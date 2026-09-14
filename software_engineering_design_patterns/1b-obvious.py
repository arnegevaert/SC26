raw_results = {}
datasets_dict = load_datasets(file_path)
for dataset_name, dataset_numpy in datasets_dict.items():
    for metric_fn in metric_fns:
        raw_results[dataset_name] = metric_fn(dataset_numpy)
benchmark_result = BenchmarkResult(raw_results)
benchmark_result.write(output_file_path)
