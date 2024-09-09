import pandas as pd
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Task 1: Define the Titanic dataset within the Seaborn library.
df=sns.load_dataset("titanic")
df.head()
df.shape   #(number_of_row,number_of_column)

# Task 2: Find the number of male and female passengers in the Titanic dataset defined above.
df["sex"].value_counts()

# Task 3: Find the number of unique values for each column.
df.nunique()

# Task 4: Find the unique values of the pclass variable.
df["pclass"].nunique()

# Task 5: Find the number of unique values of the pclass and parch variables.
df[["pclass","parch"]].nunique()   #must be numpy array inside!

# Task 6: Check the type of the embarked variable. Change its type to category. Check the type again.
df["embarked"].dtype
df["embarked"]=df["embarked"].astype("category")
df["embarked"].dtype
