# Data Preprocessing

# Import a Dataset
dataset = read.csv('Data.csv')

# Taking care a missing data
  # if is.na = if the value is N/A it will return true
  # take care of the missing age
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),  
                     dataset$Age)
  # take care of the missing salary
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)