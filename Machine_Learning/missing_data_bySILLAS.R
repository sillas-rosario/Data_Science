# Data Preprocessing

# Importing the dataset

dataset = read.csv('Data.csv')



# o codigo abaixo inicia com o datasert$age, ou seja estamos importando 
# toda coluna Age do data set.
# apos isso usamos o ifelse(declaraçao = se verdade entao executa um dos proximos metodos, yes,no)
# declaraçao = is.na(dataset$Age) ,  na = NaN , 
# caso exista um NaN  entao funcao ave é chamada 
# ave(x, ... , Fun = mean )
# ave(dataset$Age, Fun= Function(x)mean(x,na.rm = true))


dataset$Age=ifelse(is.na(dataset$Age),
                   ave(dataset$Age, FUN = function(x)mean(x,na.rm = TRUE)),
                   dataset$Age)

dataset$Salary=ifelse(is.na(dataset$Salary),
                   ave(dataset$Salary, FUN = function(x)mean(x,na.rm = TRUE)),
                   dataset$Salary)