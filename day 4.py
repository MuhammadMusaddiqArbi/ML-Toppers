import numpy as np

np_sales_data = np.array([
    [200, 220, 250, 210, 180, 190],
    [230, 240, 260, 200, 195, 205],
    [210, 215, 235, 220, 185, 200],
    [205, 210, 230, 215, 190, 195],
    [235, 245, 265, 200, 210, 218],
    [225, 235, 270, 215, 180, 215],
    [230, 245, 260, 240, 210, 220],
    [245, 255, 290, 250, 215, 225],
    [255, 265, 300, 260, 220, 230],
    [265, 275, 310, 270, 225, 235]
])

total_sales_per_product = np.sum(np_sales_data, axis=0)
print("Total sales per product:", total_sales_per_product)

average_daily_sales_per_product = np.mean(np_sales_data, axis=0)
print("Average daily sales per product:", average_daily_sales_per_product)

sales_with_commission = np_sales_data * 1.05
print("Sales with 5% commission:")
print(sales_with_commission)

sqrt_sales = np.sqrt(np_sales_data)
print("Square root of all sales values:")
print(sqrt_sales)


bonus_array = np.array([10, 20, 15, 25, 30, 5])
sales_with_bonus_array = np_sales_data + bonus_array
print("Sales with bonus_array added:")
print(sales_with_bonus_array)

sales_with_flat_bonus = np_sales_data + 50
print("Sales with $50 flat bonus added:")
print(sales_with_flat_bonus)


mean_data = np.mean(np_sales_data)
median_data = np.median(np_sales_data)
variance_data = np.var(np_sales_data)
std_dev_data = np.std(np_sales_data)
print(f"Mean of dataset: {mean_data:.2f}")
print(f"Median of dataset: {median_data:.2f}")
print(f"Variance of dataset: {variance_data:.2f}")
print(f"Standard deviation of dataset: {std_dev_data:.2f}")

max_sale = np.max(np_sales_data)
min_sale = np.min(np_sales_data)
data_range = max_sale - min_sale
print(f"Maximum sale value: {max_sale}")
print(f"Minimum sale value: {min_sale}")
print(f"Range of sales: {data_range}")

Q1 = np.percentile(np_sales_data, 25)
Q3 = np.percentile(np_sales_data, 75)
IQR = Q3 - Q1
print(f"Interquartile Range (IQR): {IQR:.2f}")


sales_greater_than_250 = np_sales_data[np_sales_data > 250]
print("Sales greater than $250:", sales_greater_than_250)

capped_sales_data = np.copy(np_sales_data)
capped_sales_data[capped_sales_data > 300] = 300
print("Sales with values > $300 capped at $300:")
print(capped_sales_data)

count_between_200_250 = np.sum((np_sales_data >= 200) & (np_sales_data <= 250))
print("Count of sales between $200 and $250:", count_between_200_250)

sales_below_mean = np_sales_data[np_sales_data < mean_data]
print("Sales below the mean:")
print(sales_below_mean)


sales_day_5 = np_sales_data[4, :]
sorted_sales_day_5 = np.sort(sales_day_5)
print("Sorted sales of Day 5:", sorted_sales_day_5)

total_sales_per_day = np.sum(np_sales_data, axis=1)
day_with_highest_sales_index = np.argmax(total_sales_per_day)
print("Day with the highest total sales (0-indexed):", day_with_highest_sales_index)
print("Total sales for that day:", total_sales_per_day[day_with_highest_sales_index])

column_wise_means = np.mean(np_sales_data, axis=0)
print("Column-wise means (average per product):", column_wise_means)

row_wise_means = np.mean(np_sales_data, axis=1)
print("Row-wise means (average per day):", row_wise_means)

overall_average_sale = np.mean(np_sales_data)
print(f"Overall average sale: {overall_average_sale:.2f}")


def highlight_outliers(data):
    mean_val = np.mean(data)
    std_val = np.std(data)
    lower_bound = mean_val - 2 * std_val
    upper_bound = mean_val + 2 * std_val
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers

outliers_in_data = highlight_outliers(np_sales_data)
print("Outliers (values 2 standard deviations above or below the mean):")
print(outliers_in_data)
