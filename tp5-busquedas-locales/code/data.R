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

# 8 queens
hillClimbing8 = filter(local_df, algorithm_name == "hillClimbing", n_queens == 8)
simulatedAnnealing8 = filter(local_df, algorithm_name == "simulatedAnnealing", n_queens == 8)
genetic8 = filter(local_df, algorithm_name == "genetic", n_queens == 8)

# Somehow gives the actual percentage
hC8percentageTrue <- mean(hillClimbing8$solution_found) * 100
sA8percentageTrue <- mean(simulatedAnnealing8$solution_found) * 100
g8percentageTrue <- mean(genetic8$solution_found) * 100

hC8meanTime <- mean(hillClimbing8$time_taken)
sA8meanTime <- mean(simulatedAnnealing8$time_taken)
g8meanTime <- mean(genetic8$time_taken)

hC8sdTime <- sd(hillClimbing8$time_taken)
sA8sdTime <- sd(simulatedAnnealing8$time_taken)
g8sdTime <- sd(genetic8$time_taken)

hC8meanStates <- mean(hillClimbing8$explored_states)
sA8meanStates <- mean(simulatedAnnealing8$explored_states)
g8meanStates <- mean(genetic8$explored_states)

hC8sdStates <- sd(hillClimbing8$explored_states)
sA8sdStates <- sd(simulatedAnnealing8$explored_states)
g8sdStates <- sd(genetic8$explored_states)

# 10 queens
hillClimbing10 = filter(local_df, algorithm_name == "hillClimbing", n_queens == 10)
simulatedAnnealing10 = filter(local_df, algorithm_name == "simulatedAnnealing", n_queens == 10)
genetic10 = filter(local_df, algorithm_name == "genetic", n_queens == 10)

# Somehow gives the actual percentage
hC10percentageTrue <- mean(hillClimbing10$solution_found) * 100
sA10percentageTrue <- mean(simulatedAnnealing10$solution_found) * 100
g10percentageTrue <- mean(genetic10$solution_found) * 100

hC10meanTime <- mean(hillClimbing10$time_taken)
sA10meanTime <- mean(simulatedAnnealing10$time_taken)
g10meanTime <- mean(genetic10$time_taken)

hC10sdTime <- sd(hillClimbing10$time_taken)
sA10sdTime <- sd(simulatedAnnealing10$time_taken)
g10sdTime <- sd(genetic10$time_taken)

hC10meanStates <- mean(hillClimbing10$explored_states)
sA10meanStates <- mean(simulatedAnnealing10$explored_states)
g10meanStates <- mean(genetic10$explored_states)

hC10sdStates <- sd(hillClimbing10$explored_states)
sA10sdStates <- sd(simulatedAnnealing10$explored_states)
g10sdStates <- sd(genetic10$explored_states)
