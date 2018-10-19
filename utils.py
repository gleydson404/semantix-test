def export_query_to_csv(data_frame, file_name):
    data_frame.coalesce(1).write.mode('overwrite').csv('results/' + file_name)

def export_all_queries_to_csv(data_frames):
    for key, value in data_frames.items():
        export_query_to_csv(value, key)

def full_file_path_by_month(files_list, month_name='jul'):
    file_by_name = [item for item in files_list if month_name.upper() in item.upper()]
    if file_by_name[0]:
        return 'data/' + file_by_name[0]
    else:
        return None
