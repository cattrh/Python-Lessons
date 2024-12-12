import pandas as pd
print('\n#1')


df = pd.read_csv('./NISPUF17.csv', sep=',')
# print(df['EDUC1'].unique())
# print(df['EDUC1'].where(df['EDUC1'] == 1).count())


def proportion_of_education(dataframe):

    len_of_df = len(df)
    less_than_12 = round(float(df['EDUC1'].where(
        df['EDUC1'] == 1).count() / len_of_df), 2)
    e12 = round(float(df['EDUC1'].where(
        df['EDUC1'] == 2).count() / len_of_df), 2)
    more_than_12 = round(float(df['EDUC1'].where(
        df['EDUC1'] == 3).count() / len_of_df), 2)
    college = round(float(df['EDUC1'].where(
        df['EDUC1'] == 4).count() / len_of_df), 2)

    pror = {"less than high school": less_than_12,
            "high school": e12,
            "more than high school but not college": more_than_12,
            "college": college}

    print(pror)


proportion_of_education(df)




# file = './NISPUF17.csv'
# df = pd.read_csv(file, sep=',')
# # df['CBF_01'] = df['CBF_01'].replace(1, 'yes', regex=True)
# # df['CBF_01'] = df['CBF_01'].replace(2, 'no', regex=True)
# # df['CBF_01'] = df['CBF_01'].replace(77, 'dk', regex=True)
# # df['CBF_01'] = df['CBF_01'].replace(99, 'miss', regex=True)

# bm = df.groupby('CBF_01')['P_NUMFLU'].mean()
# bm_tuple = (round(float(bm[1]), 1), round(float(bm[2]), 1))
# print(bm_tuple)


df = pd.read_csv('./NISPUF17.csv', sep=',')
df = df.dropna(subset=['P_NUMFLU'])
bm = df.groupby('CBF_01')['P_NUMFLU'].mean()
print(round(float(bm[1]), 1), round(float(bm[2]), 1))




file = 'NISPUF17.csv'


def chickenpox_by_sex(file):
    df = pd.read_csv(file, sep=',')
    count_male = len(df.query('(HAD_CPOX <= 2) and (SEX == 1) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    count_male_not_sick = len(df.query('(HAD_CPOX == 2) and (SEX == 1) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    count_female = len(df.query('(HAD_CPOX <= 2) and (SEX == 2) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    count_female_not_sick = len(df.query('(HAD_CPOX == 2) and (SEX == 2) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    vaccine_effectiveness = {'male': round(count_male_not_sick/count_male, 2),
                             'female': round(count_female_not_sick/count_female, 2)}
    print(vaccine_effectiveness)


chickenpox_by_sex(file)