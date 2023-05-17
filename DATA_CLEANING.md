# DATA CLEANING IN POWER QUERY

#### FIRST YOU NEED TO OPEN POWER QUERY FROM POWER BI YOU CAN DO IT WHEN IMPORTING FILE OR BY USING THE TRANSFORM DATA BUTTON


### ~TMPCLP555981 : 

 

  let 

      Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\ELL_2021_2022.accdb"), [CreateNavigationProperties=true]), 

      #"_~TMPCLP555981" = Source{[Schema="",Item="~TMPCLP555981"]}[Data], 

      MODIF1 = Table.ReplaceValue(#"_~TMPCLP555981","-","0",Replacer.ReplaceValue,{"NUM_SWD", "NUM_ECDIS"}), 

      MODIF2 = Table.ReplaceValue(MODIF1, " ", "0", Replacer.ReplaceValue, {"PER_SWD", "PER_ECDIS"}), 

      MODIF3 = Table.TransformColumnTypes(MODIF2, {{"NUM_SWD", Decimal.Type}, {"NUM_ECDIS", Decimal.Type}, {"PER_SWD", Decimal.Type}, {"PER_ECDIS",  Decimal.Type}}) 

  in 

      MODIF3 

 

 

### 2021-22 ELL Home Languages 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\ELL_2021_2022.accdb"), [CreateNavigationProperties=true]), 

    #"_2021-22 ELL Home Languages" = Source{[Schema="",Item="2021-22 ELL Home Languages"]}[Data], 

    MODIF1 = Table.TransformColumnTypes(#"_2021-22 ELL Home Languages", {"LANGUAGE_RANK", Int64.Type}) 

in 

    MODIF1 

 

### 2021-22 ELL Enrollment 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\ELL_2021_2022.accdb"), [CreateNavigationProperties=true]), 

    #"_2021-22 ELL Enrollment" = Source{[Schema="",Item="2021-22 ELL Enrollment"]}[Data], 

     

    MODIF1 = Table.ReplaceValue(#"_2021-22 ELL Enrollment","-","",Replacer.ReplaceValue,{"NUM_SWD","PER_SWD", "NUM_ECDIS", "PER_ECDIS"}),   

    #"Valeur remplacée" = Table.ReplaceValue(MODIF1,".",",",Replacer.ReplaceText,{"PER_SWD","PER_ECDIS"}),  

    MODIF3 = Table.TransformColumnTypes(#"Valeur remplacée", {{"NUM_SWD", Int64.Type},{"PER_SWD", Decimal.Type},{"NUM_ECDIS", Int64.Type},{"PER_ECDIS", Decimal.Type}})  

  

in  

  

    MODIF3 

 

### GRAD_RATE_AND_OUTCOMES_2022 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\GRAD_RATE_AND_OUTCOMES_2022.mdb"), [CreateNavigationProperties=true]), 

    _GRAD_RATE_AND_OUTCOMES_2022 = Source{[Schema="",Item="GRAD_RATE_AND_OUTCOMES_2022"]}[Data], 

  

    VALUETRANS = Table.ReplaceValue(_GRAD_RATE_AND_OUTCOMES_2022, "-", "",Replacer.ReplaceValue, {"enroll_cnt","grad_cnt","grad_pct","local_cnt", "local_pct", "reg_cnt", "reg_pct", "reg_adv_cnt", "reg_adv_pct", "non_diploma_credential_cnt", "non_diploma_credential_pct", "still_enr_cnt", "still_enr_pct", "ged_cnt", "ged_pct", "dropout_cnt", "dropout_pct"}), 

    TRANSTYPE = Table.TransformColumnTypes(VALUETRANS, {{"enroll_cnt", Int64.Type}, {"grad_cnt", Int64.Type}, {"grad_pct", Percentage.Type}, {"local_cnt",Int64.Type}, {"local_pct", Percentage.Type}, { "reg_cnt", Int64.Type}, {"reg_pct", Percentage.Type}, { "reg_adv_cnt", Int64.Type}, {"reg_adv_pct", Percentage.Type}, { "non_diploma_credential_cnt", Int64.Type}, {"non_diploma_credential_pct", Percentage.Type}, { "still_enr_cnt", Int64.Type}, {"still_enr_pct", Percentage.Type}, {"ged_cnt", Int64.Type}, {"ged_pct", Percentage.Type}, {"dropout_cnt", Int64.Type}, {"dropout_pct", Percentage.Type} }) 

    

in 

    TRANSTYPE 

 

### ACC EM ELP 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC EM ELP" = Source{[Schema="",Item="ACC EM ELP"]}[Data], 

  

    TRANSVALUE = Table.ReplaceValue(#"_ACC EM ELP", "s", "", Replacer.ReplaceValue, {"ELL_COUNT", "BENCHMARK", "PROGRESS_RATE", "SUCCESS_RATIO", "LEVEL"}), 

  

    TRANSVALUE2 = Table.ReplaceValue(TRANSVALUE, ".", ",", Replacer.ReplaceText, {"SUCCESS_RATIO"}), 

  

    TRANSTYPE = Table.TransformColumnTypes(TRANSVALUE2, {{"ELL_COUNT", Int64.Type}, {"BENCHMARK", Int64.Type},{"PROGRESS_RATE", Int64.Type},{"SUCCESS_RATIO", Decimal.Type}, {"LEVEL", Int64.Type}}) 

  

in 

     

    TRANSTYPE 

 

### ACC EM Chronic Absenteeism 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC EM Chronic Absenteeism" = Source{[Schema="",Item="ACC EM Chronic Absenteeism"]}[Data], 

  

    TRANSVALUE = Table.ReplaceValue(#"_ACC EM Chronic Absenteeism", "s", "", Replacer.ReplaceValue, {"ENROLLMENT", "ABSENT_COUNT", "ABSENT_RATE"}), 

    TRANSVALUE2 = Table.ReplaceValue(TRANSVALUE, ".", ",", Replacer.ReplaceText, {"ABSENT_RATE"}), 

    TRANSTYPE = Table.TransformColumnTypes(TRANSVALUE2, {{"ENROLLMENT", Int64.Type}, {"ABSENT_COUNT", Int64.Type}, {"ABSENT_RATE", Decimal.Type}}) 

  

in 

    TRANSTYPE 

 

### ACC EM Core and Weighted Performance 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC EM Core and Weighted Performance" = Source{[Schema="",Item="ACC EM Core and Weighted Performance"]}[Data], 

  

    TRANSVALUE = Table.ReplaceValue(#"_ACC EM Core and Weighted Performance", "s", "", Replacer.ReplaceValue, {"CORE_COHORT", "CORE_INDEX", "CORE_LEVEL", "WEIGHTED_COHORT", "WEIGHTED_INDEX", "WGT_LEVEL"}),  

  

    TRANSVALUE2 = Table.ReplaceValue(TRANSVALUE, ".", ",", Replacer.ReplaceText, {"CORE_COHORT", "CORE_INDEX", "CORE_LEVEL", "WEIGHTED_COHORT", "WEIGHTED_INDEX", "WGT_LEVEL"}), 

  

    TRANSTYPE = Table.TransformColumnTypes(TRANSVALUE2, {{"CORE_COHORT", Int64.Type}, {"CORE_INDEX", Decimal.Type}, {"CORE_LEVEL", Int64.Type}, {"WEIGHTED_COHORT", Int64.Type}, {"WEIGHTED_INDEX", Decimal.Type}, {"WGT_LEVEL", Int64.Type}})  

  

in 

    TRANSTYPE 

 

### ACC HS Chronic Absenteeism 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC HS Chronic Absenteeism" = Source{[Schema="",Item="ACC HS Chronic Absenteeism"]}[Data], 

  

    TRANSVALUE = Table.ReplaceValue(#"_ACC HS Chronic Absenteeism", "s", "", Replacer.ReplaceValue, {"ENROLLMENT", "ABSENT_COUNT", "ABSENT_RATE"}), 

    TRANSVALUE2 = Table.ReplaceValue(TRANSVALUE, ".", ",", Replacer.ReplaceText, {"ABSENT_RATE"}), 

    TRANSTYPE = Table.TransformColumnTypes(TRANSVALUE2, {{"ENROLLMENT", Int64.Type}, {"ABSENT_COUNT", Int64.Type}, {"ABSENT_RATE", Decimal.Type}}) 

in 

    TRANSTYPE 

 

### ACC EM Participation Rate 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC EM Participation Rate" = Source{[Schema="",Item="ACC EM Participation Rate"]}[Data], 

  

    TV = Table.ReplaceValue(#"_ACC EM Participation Rate", "s", "", Replacer.ReplaceValue, {"COHORT","RATE","MET_95_PERCENT"}), 

    TV2 = Table.ReplaceValue(TV, ".", ",", Replacer.ReplaceText, {"RATE"}), 

    TT = Table.TransformColumnTypes(TV2, {{"COHORT", Int64.Type}, {"RATE", Decimal.Type}}) 

in 

    TT 

 

### ACC HS Core and Weighted Performance 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC HS Core and Weighted Performance" = Source{[Schema="",Item="ACC HS Core and Weighted Performance"]}[Data], 

    

   TRANSVALUE = Table.ReplaceValue(#"_ACC HS Core and Weighted Performance", "s", "", Replacer.ReplaceValue, {"CORE_COHORT", "CORE_INDEX", "CORE_LEVEL", "WEIGHTED_COHORT", "WEIGHTED_INDEX", "WGT_LEVEL"}),    

    TRANSVALUE2 = Table.ReplaceValue(TRANSVALUE, ".", ",", Replacer.ReplaceText, {"CORE_COHORT", "CORE_INDEX", "CORE_LEVEL", "WEIGHTED_COHORT", "WEIGHTED_INDEX", "WGT_LEVEL"}),   

    TRANSTYPE = Table.TransformColumnTypes(TRANSVALUE2, {{"CORE_COHORT", Int64.Type}, {"CORE_INDEX", Decimal.Type}, {"CORE_LEVEL", Int64.Type}, {"WEIGHTED_COHORT", Int64.Type}, {"WEIGHTED_INDEX", Decimal.Type}, {"WGT_LEVEL", Int64.Type}})   

in  

    TRANSTYPE 

 

### ACC HS ELP 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC HS ELP" = Source{[Schema="",Item="ACC HS ELP"]}[Data], 

     

    TRANSVALUE = Table.ReplaceValue(#"_ACC HS ELP", "s", "", Replacer.ReplaceValue, {"ELL_COUNT", "BENCHMARK", "PROGRESS_RATE", "SUCCESS_RATIO", "LEVEL"}),  

    TRANSVALUE2 = Table.ReplaceValue(TRANSVALUE, ".", ",", Replacer.ReplaceText, {"SUCCESS_RATIO"}),  

    TRANSTYPE = Table.TransformColumnTypes(TRANSVALUE2, {{"ELL_COUNT", Int64.Type}, {"BENCHMARK", Int64.Type},{"PROGRESS_RATE", Int64.Type},{"SUCCESS_RATIO", Decimal.Type}, {"LEVEL", Int64.Type}})  

 

in  

 

    TRANSTYPE 

 

### ACC HS Participation Rate 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC HS Participation Rate" = Source{[Schema="",Item="ACC HS Participation Rate"]}[Data], 

     

     

    TV = Table.ReplaceValue(#"_ACC HS Participation Rate", "s", "", Replacer.ReplaceValue, {"COHORT","RATE","MET_95_PERCENT"}),  

    TV2 = Table.ReplaceValue(TV, ".", ",", Replacer.ReplaceText, {"RATE"}),  

    TT = Table.TransformColumnTypes(TV2, {{"COHORT", Int64.Type}, {"RATE", Decimal.Type}})  

in  

    TT 

 

### ACC HS Graduation Rate 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_ACC HS Graduation Rate" = Source{[Schema="",Item="ACC HS Graduation Rate"]}[Data], 

    

    MODIF1 = Table.ReplaceValue(#"_ACC HS Graduation Rate","s","",Replacer.ReplaceValue,{"COHORT_COUNT","GRAD_COUNT","GRAD_RATE","COHORT_LEVEL"}), 

    #"Valeur remplacée" = Table.ReplaceValue(MODIF1,".",",",Replacer.ReplaceText,{"GRAD_RATE"}), 

    MODIF3 = Table.TransformColumnTypes(#"Valeur remplacée", {{"COHORT_COUNT", Int64.Type},{"GRAD_COUNT", Int64.Type},{"GRAD_RATE", Decimal.Type}, {"COHORT_LEVEL", Int64.Type}}) 

     

in 

    MODIF3 

 

### Annual EM ELA 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Annual EM ELA" = Source{[Schema="",Item="Annual EM ELA"]}[Data], 

    TV = Table.ReplaceValue(#"_Annual EM ELA","s", "", Replacer.ReplaceValue, {"TOTAL_COUNT", "NOT_TESTED", "PCT_NOT_TESTED", "NUM_TESTED", "PCT_TESTED", "LEVEL1_COUNT", "LEVEL1_%TESTED", "LEVEL2_COUNT", "LEVEL2_%TESTED", "LEVEL3_COUNT", "LEVEL3_%TESTED", "LEVEL4_COUNT", "LEVEL4_%TESTED", "NUM_PROF", "PER_PROF","TOTAL_SCALE_SCORES", "MEAN_SCORE" }), 

    TV2 = Table.ReplaceValue(TV,".", ",", Replacer.ReplaceText, {"TOTAL_COUNT", "NOT_TESTED", "PCT_NOT_TESTED", "NUM_TESTED", "PCT_TESTED", "LEVEL1_COUNT", "LEVEL1_%TESTED", "LEVEL2_COUNT", "LEVEL2_%TESTED", "LEVEL3_COUNT", "LEVEL3_%TESTED", "LEVEL4_COUNT", "LEVEL4_%TESTED", "NUM_PROF", "PER_PROF","TOTAL_SCALE_SCORES", "MEAN_SCORE" }), 

    TT = Table.TransformColumnTypes(TV2, {{"TOTAL_COUNT", Int64.Type}, {"NOT_TESTED", Int64.Type}, {"PCT_NOT_TESTED", Decimal.Type}, {"NUM_TESTED", Int64.Type}, {"PCT_TESTED", Decimal.Type}, {"LEVEL1_COUNT", Int64.Type}, {"LEVEL1_%TESTED", Decimal.Type}, {"LEVEL2_COUNT", Int64.Type}, {"LEVEL2_%TESTED", Decimal.Type}, {"LEVEL3_COUNT", Int64.Type}, {"LEVEL3_%TESTED", Decimal.Type}, {"LEVEL4_COUNT", Int64.Type}, {"LEVEL4_%TESTED", Decimal.Type}, {"NUM_PROF", Int64.Type},{"PER_PROF", Decimal.Type},{"TOTAL_SCALE_SCORES", Int64.Type}, {"MEAN_SCORE", Int64.Type}}) 

in 

    TT 

 

### Annual EM MATH 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Annual EM MATH" = Source{[Schema="",Item="Annual EM MATH"]}[Data], 

    TV = Table.ReplaceValue(#"_Annual EM MATH","s", "", Replacer.ReplaceValue, {"TOTAL_COUNT", "NOT_TESTED", "PCT_NOT_TESTED", "NUM_TESTED", "PCT_TESTED", "LEVEL1_COUNT", "LEVEL1_%TESTED", "LEVEL2_COUNT", "LEVEL2_%TESTED", "LEVEL3_COUNT", "LEVEL3_%TESTED", "LEVEL4_COUNT", "LEVEL4_%TESTED","LEVEL5_COUNT", "LEVEL5_%TESTED", "NUM_PROF", "PER_PROF","TOTAL_SCALE_SCORES", "MEAN_SCORE", "TOTAL_EXEMPT", "NUM_EXEMPT_NTEST", "PCT_EXEMPT_NTEST", "NUM_EXEMPT_TEST", "PCT_EXEMPT_TEST" }), 

    TV2 = Table.ReplaceValue(TV,".", ",", Replacer.ReplaceText, {"TOTAL_COUNT", "NOT_TESTED", "PCT_NOT_TESTED", "NUM_TESTED", "PCT_TESTED", "LEVEL1_COUNT", "LEVEL1_%TESTED", "LEVEL2_COUNT", "LEVEL2_%TESTED", "LEVEL3_COUNT", "LEVEL3_%TESTED", "LEVEL4_COUNT", "LEVEL4_%TESTED","LEVEL5_COUNT", "LEVEL5_%TESTED", "NUM_PROF", "PER_PROF","TOTAL_SCALE_SCORES", "MEAN_SCORE", "TOTAL_EXEMPT", "NUM_EXEMPT_NTEST", "PCT_EXEMPT_NTEST", "NUM_EXEMPT_TEST", "PCT_EXEMPT_TEST" }), 

    TT = Table.TransformColumnTypes(TV2, {{"TOTAL_COUNT", Int64.Type}, {"NOT_TESTED", Int64.Type}, {"PCT_NOT_TESTED", Decimal.Type}, {"NUM_TESTED", Int64.Type}, {"PCT_TESTED", Decimal.Type}, {"LEVEL1_COUNT", Int64.Type}, {"LEVEL1_%TESTED", Decimal.Type}, {"LEVEL2_COUNT", Int64.Type}, {"LEVEL2_%TESTED", Decimal.Type}, {"LEVEL3_COUNT", Int64.Type}, {"LEVEL3_%TESTED", Decimal.Type}, {"LEVEL4_COUNT", Int64.Type}, {"LEVEL4_%TESTED", Decimal.Type},{"LEVEL5_COUNT", Int64.Type}, {"LEVEL5_%TESTED", Decimal.Type}, {"NUM_PROF", Int64.Type},{"PER_PROF", Decimal.Type},{"TOTAL_SCALE_SCORES", Int64.Type}, {"MEAN_SCORE", Int64.Type} , {"TOTAL_EXEMPT", Int64.Type}, {"NUM_EXEMPT_NTEST", Int64.Type}, {"PCT_EXEMPT_NTEST", Decimal.Type}, {"NUM_EXEMPT_TEST", Int64.Type}, {"PCT_EXEMPT_TEST", Decimal.Type}}) 

in 

    TT 

 

### Annual EM SCIENCE 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Annual EM SCIENCE" = Source{[Schema="",Item="Annual EM SCIENCE"]}[Data], 

    TV = Table.ReplaceValue(#"_Annual EM SCIENCE","s", "", Replacer.ReplaceValue, {"TOTAL_COUNT", "NOT_TESTED", "PCT_NOT_TESTED", "NUM_TESTED", "PCT_TESTED", "LEVEL1_COUNT", "LEVEL1_%TESTED", "LEVEL2_COUNT", "LEVEL2_%TESTED", "LEVEL3_COUNT", "LEVEL3_%TESTED", "LEVEL4_COUNT", "LEVEL4_%TESTED", "NUM_PROF", "PER_PROF","TOTAL_SCALE_SCORES", "MEAN_SCORE", "TOTAL_EXEMPT", "NUM_EXEMPT_NTEST", "PCT_EXEMPT_NTEST", "NUM_EXEMPT_TEST", "PCT_EXEMPT_TEST" }), 

    TV2 = Table.ReplaceValue(TV,".", ",", Replacer.ReplaceText, {"TOTAL_COUNT", "NOT_TESTED", "PCT_NOT_TESTED", "NUM_TESTED", "PCT_TESTED", "LEVEL1_COUNT", "LEVEL1_%TESTED", "LEVEL2_COUNT", "LEVEL2_%TESTED", "LEVEL3_COUNT", "LEVEL3_%TESTED", "LEVEL4_COUNT", "LEVEL4_%TESTED", "NUM_PROF", "PER_PROF","TOTAL_SCALE_SCORES", "MEAN_SCORE", "TOTAL_EXEMPT", "NUM_EXEMPT_NTEST", "PCT_EXEMPT_NTEST", "NUM_EXEMPT_TEST", "PCT_EXEMPT_TEST" }), 

    TT = Table.TransformColumnTypes(TV2, {{"TOTAL_COUNT", Int64.Type}, {"NOT_TESTED", Int64.Type}, {"PCT_NOT_TESTED", Decimal.Type}, {"NUM_TESTED", Int64.Type}, {"PCT_TESTED", Decimal.Type}, {"LEVEL1_COUNT", Int64.Type}, {"LEVEL1_%TESTED", Decimal.Type}, {"LEVEL2_COUNT", Int64.Type}, {"LEVEL2_%TESTED", Decimal.Type}, {"LEVEL3_COUNT", Int64.Type}, {"LEVEL3_%TESTED", Decimal.Type}, {"LEVEL4_COUNT", Int64.Type}, {"LEVEL4_%TESTED", Decimal.Type}, {"NUM_PROF", Int64.Type},{"PER_PROF", Decimal.Type},{"TOTAL_SCALE_SCORES", Int64.Type}, {"MEAN_SCORE", Int64.Type} , {"TOTAL_EXEMPT", Int64.Type}, {"NUM_EXEMPT_NTEST", Int64.Type}, {"PCT_EXEMPT_NTEST", Decimal.Type}, {"NUM_EXEMPT_TEST", Int64.Type}, {"PCT_EXEMPT_TEST", Decimal.Type}}) 

in 

    TT 

 

### Annual NYSAA 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Annual NYSAA" = Source{[Schema="",Item="Annual NYSAA"]}[Data],   

    TV = Table.ReplaceValue(#"_Annual NYSAA","s", "", Replacer.ReplaceValue, {"TOTAL", "NOT_TESTED", "NOT_TESTED_PER","EXEMPT","EXEMPT_PER", "TESTED", "PER_TESTED", "LEVEL1_COUNT", "LEVEL1_PER", "LEVEL2_COUNT", "LEVEL2_PER", "LEVEL3_COUNT", "LEVEL3_PER", "LEVEL4_COUNT", "LEVEL4_PER", "PROFICIENT_COUNT", "PROFICIENT_PER" }),  

    TV2 = Table.ReplaceValue(TV,".", ",", Replacer.ReplaceText, {"TOTAL", "NOT_TESTED", "NOT_TESTED_PER","EXEMPT","EXEMPT_PER", "TESTED", "PER_TESTED", "LEVEL1_COUNT", "LEVEL1_PER", "LEVEL2_COUNT", "LEVEL2_PER", "LEVEL3_COUNT", "LEVEL3_PER", "LEVEL4_COUNT", "LEVEL4_PER",  "PROFICIENT_COUNT", "PROFICIENT_PER" }),  

    TT = Table.TransformColumnTypes(TV2, {{"TOTAL", Int64.Type}, {"NOT_TESTED", Int64.Type}, {"NOT_TESTED_PER", Decimal.Type}, {"EXEMPT", Int64.Type}, {"EXEMPT_PER", Decimal.Type}, {"TESTED", Int64.Type}, {"PER_TESTED", Decimal.Type}, {"LEVEL1_COUNT", Int64.Type}, {"LEVEL1_PER", Decimal.Type}, {"LEVEL2_COUNT", Int64.Type}, {"LEVEL2_PER", Decimal.Type}, {"LEVEL3_COUNT", Int64.Type}, {"LEVEL3_PER", Decimal.Type}, {"LEVEL4_COUNT", Int64.Type}, {"LEVEL4_PER", Decimal.Type},{"PROFICIENT_COUNT", Int64.Type}, {"PROFICIENT_PER", Decimal.Type}})  

in  

    TT 

 

### Annual NYSESLAT 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Annual NYSESLAT" = Source{[Schema="",Item="Annual NYSESLAT"]}[Data], 

    TV = Table.ReplaceValue(#"_Annual NYSESLAT","s", "", Replacer.ReplaceValue, {"TOTAL", "NOT_TESTED", "PER_NTEST", "TESTED", "PER_TEST", "NUM_ENT", "PER_ENT","NUM_EMER","PER_EMER","NUM_TRAN","PER_TRAN","NUM_EXP","PER_EXP","NUM_COM","PER_COM"}),  

    TV2 = Table.ReplaceValue(TV,".", ",", Replacer.ReplaceText, {"TOTAL", "NOT_TESTED", "PER_NTEST", "TESTED", "PER_TEST", "NUM_ENT", "PER_ENT","NUM_EMER","PER_EMER","NUM_TRAN","PER_TRAN","NUM_EXP","PER_EXP","NUM_COM","PER_COM"}),  

    TT = Table.TransformColumnTypes(TV2, {{"TOTAL", Int64.Type}, {"NOT_TESTED", Int64.Type}, {"PER_NTEST", Decimal.Type}, {"TESTED", Int64.Type}, {"PER_TEST", Decimal.Type}, {"NUM_ENT", Int64.Type}, {"PER_ENT", Decimal.Type}, {"NUM_EMER", Int64.Type}, {"PER_EMER", Decimal.Type}, {"NUM_TRAN", Int64.Type}, {"PER_TRAN", Decimal.Type}, {"NUM_EXP", Int64.Type}, {"PER_EXP", Decimal.Type}, {"NUM_COM", Int64.Type}, {"PER_COM", Decimal.Type}}) 

in  

    TT 

 

 

### Annual Regents Exams 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Annual Regents Exams" = Source{[Schema="",Item="Annual Regents Exams"]}[Data], 

    TV = Table.ReplaceValue(#"_Annual Regents Exams", "s","", Replacer.ReplaceValue, {"TESTED","NUM_LEVEL1","PER_LEVEL1","NUM_LEVEL2","PER_LEVEL2","NUM_LEVEL3","PER_LEVEL3","NUM_LEVEL4","PER_LEVEL4","NUM_LEVEL5","PER_LEVEL5","NUM_PROF","PER_PROF","TOTAL_EXEMPT","NUM_EXEMPT_NTEST","PCT_EXEMPT_NTEST","NUM_EXEMPT_TEST","PCT_EXEMPT_TEST"}), 

    TV2 = Table.ReplaceValue(TV, ".",",", Replacer.ReplaceText, {"NUM_LEVEL1","PER_LEVEL1","NUM_LEVEL2","PER_LEVEL2","NUM_LEVEL3","PER_LEVEL3","NUM_LEVEL4","PER_LEVEL4","NUM_LEVEL5","PER_LEVEL5","NUM_PROF","PER_PROF","TOTAL_EXEMPT","NUM_EXEMPT_NTEST","PCT_EXEMPT_NTEST","NUM_EXEMPT_TEST","PCT_EXEMPT_TEST"}), 

    TT = Table.TransformColumnTypes(TV2, { {"TESTED", Int64.Type}, {"NUM_LEVEL1", Int64.Type}, {"PER_LEVEL1", Decimal.Type}, {"NUM_LEVEL2", Int64.Type}, {"PER_LEVEL2", Decimal.Type}, {"NUM_LEVEL3", Int64.Type}, {"PER_LEVEL3", Decimal.Type}, {"NUM_LEVEL4", Int64.Type}, {"PER_LEVEL4", Decimal.Type}, {"NUM_LEVEL5", Int64.Type}, {"PER_LEVEL5", Decimal.Type}, {"NUM_PROF", Int64.Type}, {"PER_PROF", Decimal.Type}, {"TOTAL_EXEMPT", Int64.Type}, {"NUM_EXEMPT_NTEST", Int64.Type}, {"PCT_EXEMPT_NTEST", Decimal.Type}, {"NUM_EXEMPT_TEST", Int64.Type}, {"PCT_EXEMPT_TEST", Decimal.Type}}) 

in 

    TT 

 

### Total Cohort Regents Exams 

 

let 

    Source = Access.Database(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\Windows Access\SRC2022.accdb"), [CreateNavigationProperties=true]), 

    #"_Total Cohort Regents Exams" = Source{[Schema="",Item="Total Cohort Regents Exams"]}[Data], 

    TV = Table.ReplaceValue(#"_Total Cohort Regents Exams", "s", "", Replacer.ReplaceValue, {"NTEST_COUNT", "NTEST_%COHORT", "TEST_COUNT", "TEST_%COHORT", "LEVEL1_COUNT", "LEVEL1_%COHORT", "LEVEL2_COUNT", "LEVEL2_%COHORT", "LEVEL3_COUNT", "LEVEL3_%COHORT", "LEVEL4_COUNT", "LEVEL4_%COHORT", "PROF_COUNT", "PROF_%COHORT","TOTAL_EXEMPT","NUM_EXEMPT_NTEST","PCT_EXEMPT_NTEST","NUM_EXEMPT_TEST","PCT_EXEMPT_TEST"}), 

    TV2 = Table.ReplaceValue(TV, ".", ",", Replacer.ReplaceText, {"NTEST_COUNT", "NTEST_%COHORT", "TEST_COUNT", "TEST_%COHORT", "LEVEL1_COUNT", "LEVEL1_%COHORT", "LEVEL2_COUNT", "LEVEL2_%COHORT", "LEVEL3_COUNT", "LEVEL3_%COHORT", "LEVEL4_COUNT", "LEVEL4_%COHORT", "PROF_COUNT", "PROF_%COHORT","TOTAL_EXEMPT","NUM_EXEMPT_NTEST","PCT_EXEMPT_NTEST","NUM_EXEMPT_TEST","PCT_EXEMPT_TEST"}), 

    TT = Table.TransformColumnTypes(TV2, {{"NTEST_COUNT", Int64.Type}, {"NTEST_%COHORT", Decimal.Type}, {"TEST_COUNT", Int64.Type}, {"TEST_%COHORT", Decimal.Type}, {"LEVEL1_COUNT", Int64.Type}, {"LEVEL1_%COHORT", Decimal.Type}, {"LEVEL2_COUNT", Int64.Type}, {"LEVEL2_%COHORT", Decimal.Type}, {"LEVEL3_COUNT", Int64.Type}, {"LEVEL3_%COHORT", Decimal.Type}, {"LEVEL4_COUNT", Int64.Type}, {"LEVEL4_%COHORT", Decimal.Type}, {"PROF_COUNT", Int64.Type}, {"PROF_%COHORT", Decimal.Type}, {"TOTAL_EXEMPT", Int64.Type},{"NUM_EXEMPT_NTEST", Int64.Type},{"PCT_EXEMPT_NTEST", Decimal.Type},{"NUM_EXEMPT_TEST", Int64.Type},{"PCT_EXEMPT_TEST", Decimal.Type}}) 

in 

    TT 

 

### ELA 

 

let 

    Source = Excel.Workbook(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\csv\3-8-ELA-MATH-REFUSALS.xlsx"), null, true), 

    ELA_Sheet = Source{[Item="ELA",Kind="Sheet"]}[Data], 

    #"En-têtes promus" = Table.PromoteHeaders(ELA_Sheet, [PromoteAllScalars=true]), 

    #"Type modifié" = Table.TransformColumnTypes(#"En-têtes promus",{{"Column1", type text}, {"Column2", type text}, {"Column3", type text}, {"Column4", type text}, {"ALL STUDENTS", Int64.Type}, {"Column6", Decimal.Type}, {"ENGLISH LANGUAGE LEARNER", Int64.Type}, {"Column8", Decimal.Type}, {"STUDENTS WITH DISABILITIES", Int64.Type}, {"Column10", Decimal.Type}, {"ECONOMICALLY DISADVANTAGED",Int64.Type}, {"Column12", Decimal.Type}}), 

    #"Colonnes renommées" = Table.RenameColumns(#"Type modifié",{{"Column1", "INSTITUTION_ID"}, {"Column2", "ENTITY_CD"}, {"Column3", "ENTITY_NAME"}, {"Column4", "SUBJECT"}, {"ALL STUDENTS", "ALL STUDENTS TOTAL_COUNT"}, {"Column6", "ALL STUDENTS %_REFUSED"}, {"ENGLISH LANGUAGE LEARNER", "ENGLISH LANGUAGE LEARNER TOTAL_COUNT"}, {"Column8", "ENGLISH LANGUAGE LEARNER %_REFUSED"}, {"Column10", "STUDENTS WITH DISABILITIES %_REFUSED"}, {"STUDENTS WITH DISABILITIES", "STUDENTS WITH DISABILITIES TOTAL_COUNT"}, {"Column12", "ECONOMICALLY DISADVANTAGED %_REFUSED"}, {"ECONOMICALLY DISADVANTAGED", "ECONOMICALLY DISADVANTAGED TOTAL_COUNT"}}), 

    #"Premières lignes supprimées" = Table.Skip(#"Colonnes renommées",1) 

in 

    #"Premières lignes supprimées" 

 

  ### MATH 

 

let 

    Source = Excel.Workbook(File.Contents("C:\Users\Travail\OneDrive - EPITA\Projet\New York succes from school\Data\2021-2022\csv\3-8-ELA-MATH-REFUSALS.xlsx"), null, true), 

    MATH_Sheet = Source{[Item="MATH",Kind="Sheet"]}[Data], 

    #"En-têtes promus" = Table.PromoteHeaders(MATH_Sheet, [PromoteAllScalars=true]), 

    #"Type modifié" = Table.TransformColumnTypes(#"En-têtes promus",{{"Column1", type text}, {"Column2", type text}, {"Column3", type text}, {"Column4", type text}, {"ALL STUDENTS", Int64.Type}, {"Column6", Decimal.Type}, {"ENGLISH LANGUAGE LEARNER", Int64.Type}, {"Column8", Decimal.Type}, {"STUDENTS WITH DISABILITIES", Int64.Type}, {"Column10", Decimal.Type}, {"ECONOMICALLY DISADVANTAGED", Int64.Type}, {"Column12", Decimal.Type}}), 

    #"Colonnes renommées" = Table.RenameColumns(#"Type modifié",{{"Column1", "INSTITUTION_ID"}, {"Column2", "ENTITY_CD"}, {"Column3", "ENTITY_NAME"}, {"Column4", "SUBJECT"}, {"Column6", "ALL STUDENTS %_REFUSED"}, {"Column8", "ENGLISH LANGUAGE LEARNER %_REFUSED"}, {"Column10", "STUDENTS WITH DISABILITIES %_REFUSED"}, {"Column12", "ECONOMICALLY DISADVANTAGED %_REFUSED"}}), 

    #"Premières lignes supprimées" = Table.Skip(#"Colonnes renommées",1) 

in 

    #"Premières lignes supprimées" 
