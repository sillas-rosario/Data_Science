

# Simple linear Regression
# first step is start with editing the template

dataset = read.csv('Salary_Data.csv')

library(caTools)

#this is the same ideia of random we've set in Pyton
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set= subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#feature scaling

training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])

#fitting linear regression to the training set

regressor = lm( formula = Salary ~ YearsExperience, data = training_set)

# predicting  the test set results

y_pred= predict(regressor, newdata = test_set)

#installing

#install.packages('ggplot2')
#library(ggplot2)

ggplot()+
  geom_point(aes(x = training_set$YearsExperience, y =training_set$Salary),
             colour ='red')+
  geom_line(aes(x=training_set$YearsExperience, y =predict(regressor, newdata = training_set)),
                colour='blue')+
  ggtitle('Salary vc Experince(Training set)')+
  xlab('')+
  ylab('')


