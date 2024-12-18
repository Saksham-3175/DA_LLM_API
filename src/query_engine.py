import pandas as pd
from sqlalchemy import create_engine
from llm_integration import generate_response

def process_query(query, dataset1_path, dataset2_path):
    try:
        #Loading the datasets
        df1 = pd.read_csv(dataset1_path)
        df2 = pd.read_csv(dataset2_path)

        #Creating a temporoary SQLite database
        engine = create_engine("sqlite:///:memory:")
        df1.to_sql("health1", engine, index=False, if_exists="replace")
        df2.to_sql("health2", engine, index=False, if_exists="replace")
        
        #Generating SQL querry dynamically
        sql_query = f"""
        SELECT * 
        FROM health1 
        INNER JOIN health2
        ON health1.Patient_Number = health2.Patient_Number
        LIMIT 10;
        """
        result = pd.read_sql(sql_query, engine)

        #Generating response from the LLM
        response = generate_response(query, result)
        return response 
    except Exception as e:
        return f"Error processing the query: {e}"