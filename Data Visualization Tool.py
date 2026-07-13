
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def visualize_data():

    file = input("Enter CSV file name: ")

    try:
        data = pd.read_csv(file)

        print("\nDataset Loaded Successfully!\n")
        print(data.head())

        while True:

            print("\n========== MENU ==========")
            print("1. Display Dataset")
            print("2. Line Chart")
            print("3. Bar Chart")
            print("4. Scatter Plot")
            print("5. Histogram")
            print("6. Box Plot")
            print("7. Correlation Heatmap")
            print("8. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                print("\nDataset:")
                print(data)

            elif choice == "2":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                plt.figure(figsize=(8,5))
                plt.plot(data[x], data[y], marker="o")
                plt.title("Line Chart")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.grid(True)
                plt.show()

            elif choice == "3":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                plt.figure(figsize=(8,5))
                sns.barplot(x=data[x], y=data[y])
                plt.title("Bar Chart")
                plt.show()

            elif choice == "4":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                plt.figure(figsize=(8,5))
                sns.scatterplot(x=data[x], y=data[y])
                plt.title("Scatter Plot")
                plt.show()

            elif choice == "5":
                column = input("Enter column name: ")

                plt.figure(figsize=(8,5))
                plt.hist(data[column], bins=10)
                plt.title("Histogram")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.show()

            elif choice == "6":
                column = input("Enter column name: ")

                plt.figure(figsize=(6,5))
                sns.boxplot(y=data[column])
                plt.title("Box Plot")
                plt.show()

            elif choice == "7":

                plt.figure(figsize=(8,6))
                sns.heatmap(data.corr(numeric_only=True),
                            annot=True,
                            cmap="coolwarm")
                plt.title("Correlation Heatmap")
                plt.show()

            elif choice == "8":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

    except FileNotFoundError:
        print("CSV File not found!")

    except Exception as e:
        print("Error:", e)


print("-+"*45)
print(" "*30 + "DATA VISUALIZATION TOOL")
print("-+"*45)

visualize_data()