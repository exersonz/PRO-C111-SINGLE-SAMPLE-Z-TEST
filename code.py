import pandas as pd
import statistics
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("population mean is {}".format(population_mean))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading time"], show_hist = False)
    fig.show()

mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)
show_fig(mean_list)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)
print("std1 start is {} and end is {}".format(first_std_deviation_start, first_std_deviation_end))
print("std2 start is {} and end is {}".format(second_std_deviation_start, second_std_deviation_end))
print("std3 start is {} and end is {}".format(third_std_deviation_start, third_std_deviation_end))

fig = ff.create_distplot([mean_list], ["sample reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STD1 START"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STD1 END"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STD2 START"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STD2 END"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STD3 START"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STD3 END"))
fig.show()

dfd = pd.read_csv("sample_2.csv")
dataa = dfd["reading_time"].tolist()
new_sample_mean = statistics.mean(dataa)
print("the new sample mean is {}".format(new_sample_mean))
fig = ff.create_distplot([dataa], ["sample reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "SAMPLE MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STD1 START"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STD1 END"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STD2 START"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STD2 END"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STD3 START"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STD3 END"))
fig.show()

z_score = (new_sample_mean - mean)/std_deviation
print("the z-score is {}".format(z_score))