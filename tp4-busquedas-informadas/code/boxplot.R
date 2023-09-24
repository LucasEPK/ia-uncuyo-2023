library(ggplot2)

no_informada_df <- readr::read_csv("https://raw.githubusercontent.com/LucasEPK/ia-uncuyo-2023/main/tp4-busquedas-informadas/informada-results.csv")

no_informada_df

# Creates a ggplot2 boxplot
ggplot(data=no_informada_df)+
  geom_boxplot(
    aes(x=algorithm_name, y=explored_states,color=algorithm_name)
  )+
  theme_classic()

library(dplyr)

bfs = filter(no_informada_df, algorithm_name== "BFS")
dfs = filter(no_informada_df, algorithm_name== "DFS")
dls = filter(no_informada_df, algorithm_name== "DLS")
ucs = filter(no_informada_df, algorithm_name== "UCS")
aStar = filter(no_informada_df, algorithm_name== "A*")

bfsMean = mean(bfs$explored_states)
dfsMean = mean(dfs$explored_states)
dlsMean = mean(dls$explored_states)
ucsMean = mean(ucs$explored_states)
aStarMean = mean(aStar$explored_states)

bfsSD = sd(bfs$explored_states)
dfsSD = sd(dfs$explored_states)
dlsSD = sd(dls$explored_states)
ucsSD = sd(ucs$explored_states)
aStarSD = sd(aStar$explored_states)