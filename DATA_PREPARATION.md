# Preparation of the DATA: Creation of new tables, columns and measures

### Creation of columns in MATH :

    NBR ALL STUDENTS REFUSED = 'MATH'[ALL STUDENTS %_REFUSED] * 'MATH'[ALL STUDENTS] / 100 

    NBR ELL REFUSED = 'MATH'[ENGLISH LANGUAGE LEARNER %_REFUSED] * 'MATH'[ENGLISH LANGUAGE LEARNER] /100 

    NBR STUDENT WITH DISABILITIES REFUSED = 'MATH'[STUDENTS WITH DISABILITIES %_REFUSED] * 'MATH'[STUDENTS WITH DISABILITIES] /100 

    NBR ECO DISADVANTAGED REFUSED = 'MATH'[ECONOMICALLY DISADVANTAGED %_REFUSED] * 'MATH'[ECONOMICALLY DISADVANTAGED] /100 

### Creation of a measure in Cohort_Pathways_2022 :

Calcul of the number of student.

    NBR STUDENT = CALCULATE(SUM(Cohort_Pathways_2022[STUDENT_COUNT]), ALLEXCEPT(Cohort_Pathways_2022, Cohort_Pathways_2022[AGGREGATION_NAME], Cohort_Pathways_2022[SUBGROUP_NAME] )) 

### Creation de la table COUNTY :
 
 Creation of a table with the school and the county and district to make relation between tables.
 
    COUNTY = SELECTCOLUMNS( 

        FILTER('BOCES and N/RC', 'BOCES and N/RC'[YEAR] = 2022), 

        "INSTITUTION_ID",'BOCES and N/RC'[INSTITUTION_ID], 

        "ENTITY_CD",'BOCES and N/RC'[ENTITY_CD], 

        "COUNTY_CD",'BOCES and N/RC'[COUNTY_CD], 

        "COUNTY_NAME", 'BOCES and N/RC'[COUNTY_NAME], 

        "DISTRICT_CD", 'BOCES and N/RC'[DISTRICT_CD], 

        "DISTRICT_NAME", 'BOCES and N/RC'[DISTRICT_NAME] 

    ) 

### Creation of measures in Inexperienced Teachers and Principals :

Calcul of the percentage of experimented teachers.
 
    PER_TEACHER_EXP = 100 - 'Inexperienced Teachers and Principals'[PER_TEACH_INEXP] 
    
Calcul of minimum and maximum (measures) of various columns in order to add min and max bar to our graphs :
    
    MAX_PER_TEACHER_EXP = CALCULATE(MAX('Inexperienced Teachers and Principals'[PER_TEACHER_EXP]), ALLEXCEPT('COUNTY', 'COUNTY'[COUNTY_NAME])) 

    MIN_PER_TEACHER_EXP = CALCULATE(MIN('Inexperienced Teachers and Principals'[PER_TEACHER_EXP]), ALLEXCEPT('COUNTY', 'COUNTY'[COUNTY_NAME])) 

    MAX_PER_TEACHER_INXP = CALCULATE(MAX('Inexperienced Teachers and Principals'[PER_TEACH_INEXP]), ALLEXCEPT('COUNTY', 'COUNTY'[COUNTY_NAME])) 

    MIN_PER_TEACHER_INXP = CALCULATE(MIN('Inexperienced Teachers and Principals'[PER_TEACH_INEXP]), ALLEXCEPT('COUNTY', 'COUNTY'[COUNTY_NAME])) 

    MIN_EXP_PER_COUNTY = CALCULATE(MIN('Expenditures per Pupil'[PER_FED_STATE_LOCAL_EXP]), ALLEXCEPT(COUNTY, COUNTY[COUNTY_NAME])) 

    MAX_EXP_PER_COUNTY = CALCULATE(MAX('Expenditures per Pupil'[PER_FED_STATE_LOCAL_EXP]), ALLEXCEPT(COUNTY, COUNTY[COUNTY_NAME])) 

    MIN_EXP_PER_COUNTY = CALCULATE(MIN('Expenditures per Pupil'[PER_FED_STATE_LOCAL_EXP]), ALLEXCEPT(COUNTY, COUNTY[COUNTY_NAME])) 

    MAX_EXP_PER_COUNTY = CALCULATE(MAX('Expenditures per Pupil'[PER_FED_STATE_LOCAL_EXP]), ALLEXCEPT(COUNTY, COUNTY[COUNTY_NAME])) 
    
### Creation of the Table NB_ELEVE :

This table contains the number of student by school and was created to create relationship between table to analyse the data.

    NB_ELEVE =  

    SELECTCOLUMNS( 

        FILTER('BEDS Day Enrollment', 'BEDS Day Enrollment'[YEAR] = 2022), 

        "ENTITY_CD",'BEDS Day Enrollment'[ENTITY_CD], 

        "ENTITY_NAME",'BEDS Day Enrollment'[ENTITY_NAME], 

        "NB_ELEVE",'BEDS Day Enrollment'[K12] 

        ) 

Adding of the measure RAPPORT_PROF_ELEVE counting the number of student for one teacher:

    RAPPORT_PROF_ELEVE =  

    CALCULATE( 

        DIVIDE( 

            SUM('NB_ELEVE'[NB_ELEVE]), 

            SUM('Inexperienced Teachers and Principals'[NUM_TEACH]) 

        ), 

        ALLEXCEPT('NB_ELEVE', NB_ELEVE[ENTITY_NAME], 'COUNTY'[COUNTY_NAME]    ) 

    ) 

### Creation of the columns with the Z-score in Annual Regents Exams :

Creation of the z score and related columns in order to create the classement.

    StandardDeviation = CALCULATE(STDEV.P('Annual Regents Exams'[PER_PROF]),ALLEXCEPT('Annual Regents Exams','Annual Regents Exams'[SUBJECT]))
    
    Mean = CALCULATE(AVERAGE('Annual Regents Exams'[PER_PROF]), ALLEXCEPT('Annual Regents Exams','Annual Regents Exams'[SUBJECT]))
    
    Z-Score_column = ('Annual Regents Exams'[PER_PROF]-'Annual Regents Exams'[Mean])/'Annual Regents Exams'[StandardDeviation]
    
    Z-SCORE_SCHOOL = CALCULATE(AVERAGE('Annual Regents Exams'[Z-Score_column]), ALLEXCEPT( 'Annual Regents Exams', 'Annual Regents Exams'[ENTITY_NAME])) 

### Creation of the CORRELATION and its measures : 

Creation of the table because of the complicated relationship between the tables in order to do the measures folowing.

    CORRELATION =  
    
      VAR instit =  

        SELECTCOLUMNS( 

            FILTER(ALL('Institution Grouping'), 'Institution Grouping'[GROUP_NAME]="Public School"), 

            "INSTITUTION_ID", 'Institution Grouping'[INSTITUTION_ID] &"1", 

            "ENTITY_CD", 'Institution Grouping'[ENTITY_CD] &"2", 

            "ENTITY_NAME", 'Institution Grouping'[ENTITY_NAME] &"3" 

            ) 

      VAR cunt =  

        SELECTCOLUMNS( 

            ALL(COUNTY), 

            "INSTITUTION_ID", COUNTY[INSTITUTION_ID] &"1", 

            "COUNTY_NAME", COUNTY[COUNTY_NAME] 

        ) 

      VAR first_tb =  

        NATURALLEFTOUTERJOIN( 

            instit, 

            cunt) 

      VAR acc = 

        SELECTCOLUMNS( 

            FILTER('Accountability Levels','Accountability Levels'[YEAR]="2022"), 

            "INSTITUTION_ID", 'Accountability Levels'[INSTITUTION_ID] &"1", 

            "AVERAGE_ACCOUNTABILITY_LEVEL", 'Accountability Levels'[AVERAGE] 

        )  

      VAR second_tb = 

        NATURALLEFTOUTERJOIN( 

            first_tb, 

            DISTINCT(acc)) 

      VAR reg =  

        SELECTCOLUMNS( 

            FILTER('Annual Regents Exams','Annual Regents Exams'[YEAR]=2022), 

            "INSTITUTION_ID", 'Annual Regents Exams'[INSTITUTION_ID] &"1", 

            "Z_score", 'Annual Regents Exams'[Z-SCORE_SCHOOL] 

        ) 

      VAR third_tb = 

        NATURALLEFTOUTERJOIN( 

            second_tb, 

            DISTINCT(reg))  

      VAR inexp =  

        SELECTCOLUMNS( 

            FILTER('Inexperienced Teachers and Principals','Inexperienced Teachers and Principals'[YEAR]=2022), 

            "INSTITUTION_ID", 'Inexperienced Teachers and Principals'[INSTITUTION_ID] &"1", 

            "PER_INEXP_TEACHER", 'Inexperienced Teachers and Principals'[PER_TEACH_INEXP], 

            "NB_STUDENT_FOR_1_TEACHER", 'Inexperienced Teachers and Principals'[RAPPORT_PROF_ELEVE] 

        )     

      VAR four_tb = 

        NATURALLEFTOUTERJOIN( 

            third_tb, 

            inexp) 

      VAR expend =  

        SELECTCOLUMNS( 

            FILTER('Expenditures per Pupil', 'Expenditures per Pupil'[YEAR]=2022), 

            "INSTITUTION_ID", 'Expenditures per Pupil'[INSTITUTION_ID] &"1", 

            "EXPENDITURE_PER_STUDENT", 'Expenditures per Pupil'[PER_FED_STATE_LOCAL_EXP] 

        ) 

      VAR five_tb = 

        NATURALLEFTOUTERJOIN( 

            four_tb, 

            expend) 

      VAR coord =  

        SELECTCOLUMNS( 

            school_names_xy_addr, 

            "ENTITY_NAME", school_names_xy_addr[Name] &"3", 

            "LATITUDE", school_names_xy_addr[Latitude], 

            "LONGITUDE", school_names_xy_addr[Longitude] 

        ) 


      VAR six_tb = 

        NATURALLEFTOUTERJOIN( 

            five_tb, 

            coord) 

      RETURN 

       six_tb 

 Creation of the measures of correlation between our points of classment :
 
    COEF_AVG_LEVEL_EXPENDITURE_PER_STUDENT =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[EXPENDITURE_PER_STUDENT])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)*('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_AVG_LEVEL_INEXP_TEACHER =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[PER_INEXP_TEACHER])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)*('CORRELATION'[PER_INEXP_TEACHER]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_AVG_LEVEL_NB_STUDENT_FOR_1_TEACHER =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[NB_STUDENT_FOR_1_TEACHER])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)*('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_CORR_GRADE_AVG_LEVEL =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[Z_score])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)*('CORRELATION'[Z_score]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[AVERAGE_ACCOUNTABILITY_LEVEL]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[Z_score]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_CORR_GRADE_EXPENDITURE_PER_STUDENT =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[EXPENDITURE_PER_STUDENT])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[Z_score])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muX)*('CORRELATION'[Z_score]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[Z_score]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_CORR_GRADE_INEXP_TEACHER =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[PER_INEXP_TEACHER])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[Z_score])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muX)*('CORRELATION'[Z_score]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[Z_score]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_CORR_GRADE_NB_STUDENT_FOR_1_TEACHER =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[NB_STUDENT_FOR_1_TEACHER])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[Z_score])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muX)*('CORRELATION'[Z_score]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[Z_score]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_CORR_INEXP_TEACHER_EXPENDITURE_PER_STUDENT =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[PER_INEXP_TEACHER])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[EXPENDITURE_PER_STUDENT])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muX)*('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_CORR_INEXP_TEACHER_NB_STUDENT_FOR_1_TEACHER =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[PER_INEXP_TEACHER])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[NB_STUDENT_FOR_1_TEACHER])) 
    //numerator 
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muX)*('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[PER_INEXP_TEACHER]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

    COEF_NB_STUDENT_FOR_1_TEACHER_EXPENDITURE_PER_STUDENT =  
    //x̄ 
    var __muX =calculate(AVERAGE('CORRELATION'[EXPENDITURE_PER_STUDENT])) 
    //ȳ 
    var __muY=calculate(AVERAGE('CORRELATION'[NB_STUDENT_FOR_1_TEACHER])) 
    //numerator
    var __numerator  =  sumx('CORRELATION',('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muX)*('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muY)) 
    //denominator 
    var __denominator=  SQRT(sumx('CORRELATION',('CORRELATION'[EXPENDITURE_PER_STUDENT]-__muX)^2)*sumx('CORRELATION',('CORRELATION'[NB_STUDENT_FOR_1_TEACHER]-__muY)^2)) 
    return 
    divide(__numerator,__denominator) 

### Creation of the Classsment table :

    CLASSEMENT =  

      VAR instit =  

        SELECTCOLUMNS( 

            FILTER(ALL('Institution Grouping'), 'Institution Grouping'[GROUP_NAME]="Public School"), 

            "INSTITUTION_ID", 'Institution Grouping'[INSTITUTION_ID] &"1", 

            "ENTITY_CD", 'Institution Grouping'[ENTITY_CD] &"2", 

            "ENTITY_NAME", 'Institution Grouping'[ENTITY_NAME] &"3" 

            )

      VAR cunt =  

        SELECTCOLUMNS( 

            ALL(COUNTY), 

            "INSTITUTION_ID", COUNTY[INSTITUTION_ID] &"1", 

            "COUNTY_NAME", COUNTY[COUNTY_NAME] 

        )   

      VAR first_tb =  

        NATURALINNERJOIN( 

            instit, 

            cunt) 

      VAR acc = 

        SELECTCOLUMNS( 

            FILTER('Accountability Levels','Accountability Levels'[YEAR]="2022"), 

            "INSTITUTION_ID", 'Accountability Levels'[INSTITUTION_ID] &"1", 

            "AVERAGE_ACCOUNTABILITY_LEVEL", 'Accountability Levels'[AVERAGE] 

        )

      VAR second_tb = 

        NATURALINNERJOIN( 

            first_tb, 

            DISTINCT(acc)) 
            
      VAR reg =  

        SELECTCOLUMNS( 

            FILTER('Annual Regents Exams','Annual Regents Exams'[YEAR]=2022), 

            "INSTITUTION_ID", 'Annual Regents Exams'[INSTITUTION_ID] &"1", 

            "Z_score", 'Annual Regents Exams'[Z-SCORE_SCHOOL] 

        ) 

      VAR third_tb = 

        NATURALINNERJOIN( 

            second_tb, 

            DISTINCT(reg)) 

      VAR inexp =  

        SELECTCOLUMNS( 

            FILTER('Inexperienced Teachers and Principals','Inexperienced Teachers and Principals'[YEAR]=2022), 

            "INSTITUTION_ID", 'Inexperienced Teachers and Principals'[INSTITUTION_ID] &"1", 

            "PER_EXP_TEACHER", 'Inexperienced Teachers and Principals'[PER_TEACHER_EXP], 

            "NB_STUDENT_FOR_1_TEACHER", 'Inexperienced Teachers and Principals'[RAPPORT_PROF_ELEVE] 

        )     

      VAR four_tb = 

        NATURALINNERJOIN( 

            third_tb, 

            inexp) 

      VAR expend =  

        SELECTCOLUMNS( 

            FILTER('Expenditures per Pupil', 'Expenditures per Pupil'[YEAR]=2022), 

            "INSTITUTION_ID", 'Expenditures per Pupil'[INSTITUTION_ID] &"1", 

            "EXPENDITURE_PER_STUDENT", 'Expenditures per Pupil'[PER_FED_STATE_LOCAL_EXP] 

        ) 

      VAR five_tb = 

        NATURALINNERJOIN( 

            four_tb, 

            expend) 
    
      VAR coord =  

        SELECTCOLUMNS( 

            school_names_xy_addr, 

            "ENTITY_NAME", school_names_xy_addr[Name] &"3", 

            "LATITUDE", school_names_xy_addr[Latitude], 

            "LONGITUDE", school_names_xy_addr[Longitude] 

        ) 

      VAR six_tb = 

        NATURALLEFTOUTERJOIN( 

            five_tb, 

            coord) 

      RETURN 

        six_tb 

 
Creation of the column CLASSSEMENT_SCORE in the table :

    CLASSSEMENT_SCORE =  
    DIVIDE(CLASSEMENT[AVERAGE_ACCOUNTABILITY_LEVEL], AVERAGE(CLASSEMENT[AVERAGE_ACCOUNTABILITY_LEVEL])) * 0.25 
    + CLASSEMENT[Z_score] * 0.3 
    + DIVIDE(CLASSEMENT[PER_EXP_TEACHER], AVERAGE(CLASSEMENT[PER_EXP_TEACHER])) * 0.15 
    + DIVIDE(CLASSEMENT[NB_STUDENT_FOR_1_TEACHER], AVERAGE(CLASSEMENT[NB_STUDENT_FOR_1_TEACHER])) * 0.2 
    + DIVIDE(CLASSEMENT[EXPENDITURE_PER_STUDENT], AVERAGE(CLASSEMENT[EXPENDITURE_PER_STUDENT])) * 0.1 

 

 
