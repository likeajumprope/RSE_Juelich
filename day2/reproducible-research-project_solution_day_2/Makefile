.PHONY: all clean_data plot_data
all: clean_data plot_data

clean_data:
	python src/clean_data.py data/raw/student_habits_performance.csv data/clean/clean.csv

plot_data:
	python src/plot_data.py data/clean/clean.csv results/plot.png