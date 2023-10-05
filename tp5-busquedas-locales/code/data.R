library(ggplot2)

local_df <- readr::read_csv("https://raw.githubusercontent.com/LucasEPK/ia-uncuyo-2023/main/tp5-busquedas-locales/locales-results.csv")

local_df

# Creates a ggplot2 boxplot
ggplot(data=local_df)+
  geom_boxplot(
    aes(x=algorithm_name, y=time_taken,color=algorithm_name)
  )+
  theme_classic()

library(dplyr)

# 4 queens
hillClimbing4 = filter(local_df, algorithm_name == "hillClimbing", n_queens == 4)
simulatedAnnealing4 = filter(local_df, algorithm_name == "simulatedAnnealing", n_queens == 4)
genetic4 = filter(local_df, algorithm_name == "genetic", n_queens == 4)

# Somehow gives the actual percentage
hC4percentageTrue <- mean(hillClimbing4$solution_found) * 100
sA4percentageTrue <- mean(simulatedAnnealing4$solution_found) * 100
g4percentageTrue <- mean(genetic4$solution_found) * 100

hC4meanTime <- mean(hillClimbing4$time_taken)
sA4meanTime <- mean(simulatedAnnealing4$time_taken)
g4meanTime <- mean(genetic4$time_taken)

hC4sdTime <- sd(hillClimbing4$time_taken)
sA4sdTime <- sd(simulatedAnnealing4$time_taken)
g4sdTime <- sd(genetic4$time_taken)

hC4meanStates <- mean(hillClimbing4$explored_states)
sA4meanStates <- mean(simulatedAnnealing4$explored_states)
g4meanStates <- mean(genetic4$explored_states)

hC4sdStates <- sd(hillClimbing4$explored_states)
sA4sdStates <- sd(simulatedAnnealing4$explored_states)
g4sdStates <- sd(genetic4$explored_states)




