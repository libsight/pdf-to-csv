import tabula
import pandas as pd


def main(input_filename: str, output_filename: str):
    dfs = tabula.read_pdf(input_filename, pages='all')

    modified_dfs = [df.rename(columns=df.iloc[2]).drop(df.index[0]).drop(df.index[1]).drop(df.index[2])for df in dfs]

    final_df = pd.concat(modified_dfs, ignore_index=True)
    final_df.to_csv(output_filename, index=False)

if __name__ == "__main__":
    main('input.pdf', 'output.csv')
