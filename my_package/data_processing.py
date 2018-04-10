import pandas as pd

def combine_seg_step(data_seg, data_steps):
    combined_data = pd.DataFrame([])
    for m in range(data_seg.shape[0]):
        # extract step series
        data_steps_series = data_seg['Step IDs'][m]
        data_steps_series = data_steps_series.split(sep = ',')
        # convert to dataframe
        data_steps_df = pd.DataFrame(data_steps_series, columns= ['Step ID'])
        # change type for float64
        data_steps_df['Step ID'] = pd.to_numeric(data_steps_df['Step ID'])
        # merge with data_steps
        data_merge = pd.merge(data_steps_df, data_steps, on='Step ID')
        combined_data = combined_data.append(data_merge, ignore_index = True)

    return combined_data