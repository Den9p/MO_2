# MO_2

1) Пока не искал аномальные значения или выбросы  
2) EdLevel - Надо обсудить - преобразовал в int значения что в будующем создаст зависимость между этими переменными, но по идее в уровне образования она и должна быть  
3) Gender - Надо обсудить - Стоит ли учитывать NonBinary вообще? Может его лучше drop и преобразовать в int (Man = 1, Woman = 0)?  
4) Country - Надо обсудить - Сделал порог для редких стран, потому что получается много стобцов с dummy переменными, но по идее все зависит от задачи  
5) HaveWorkedWith - Аналогично Country  


Data columns (total 15 columns):
    Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Unnamed: 0      73462 non-null  int64 - Удалил  
 1   Age             73462 non-null  object - Преобразовал в интовое значение и переименовал "<35 Years" (<35 = 1 и >35= 0)  
 2   Accessibility   73462 non-null  object - Преобразовал в интовое значение "Accessibility" (Yes = 1, No = 0)  
 3   EdLevel         73462 non-null  object - ['Master' 'Undergraduate' 'PhD' 'Other' 'NoHigherEd'] - Преобразовал в int 0,1,2 … - Обсудить т.к получается зависимость  
 4   Employment      73462 non-null  int64  - Преобразовал в интовое значение "Employment" (Работает = 1, не работает = 0)  
 5   Gender          73462 non-null  object - ['Man' 'Woman' 'NonBinary'] - Преобразовал в dummy переменные - Обсудить, может NonBinary убрать?  
 6   MentalHealth    73462 non-null  object - Преобразовал в интовое значение "MentalHealth" (Нет = 0, Да = 1)  
 7   MainBranch      73462 non-null  object - Преобразовал в интовое значение "Dev" (Dev = 1, NotDev = 0)  
 8   YearsCode       73462 non-null  int64  - Ничего не делал  
 9   YearsCodePro    73462 non-null  int64  - Ничего не делал  
 10  Country         73462 non-null  object - Использовал dummy переменные, предварительно сделал порог для редких стран в 500 единиц - Обсудить  
 11  PreviousSalary  73462 non-null  float64 - Ничего не делал  
 12  HaveWorkedWith  73399 non-null  object - Использовал dummy переменные, предварительно сделал порог для редких технологий в 5000 шт - Обсудить  
 13  ComputerSkills  73462 non-null  int64 - Ничего не делал  
 14  Employed        73462 non-null  int64 - Ничего не делал  
