class UrlMatcher:

    def load_raw_urls(self):
        import connection_manager.oracle_connection_manager as cm
        import traceback
        import pandas as pd

        try:
            conn_handler = cm.ManageConnection()
            conn = conn_handler.create_connection()

            sql_stmt = 'select * from raw_data'
            raw_data_df = pd.read_sql(sql_stmt, con=conn)
            return raw_data_df

        except Exception as e:
            traceback.print_exc(e)

        finally:
            conn_handler.distroy_connection()

    def load_matched_urls(self):
        import connection_manager.oracle_connection_manager as cm
        import traceback
        import pandas as pd

        try:
            conn_handler = cm.ManageConnection()
            conn = conn_handler.create_connection()

            sql_stmt = 'select * from matched_data'
            matched_data_df = pd.read_sql(sql_stmt, con=conn)
            return matched_data_df

        except Exception as e:
            traceback.print_exc(e)

        finally:
            conn_handler.distroy_connection()

    def url_matcher(self):

        matched_data_df =

if __name__ == '__main__':
    url_matcher = UrlMatcher()
    url_matcher.load_raw_urls()
    url_matcher.load_matched_urls()
