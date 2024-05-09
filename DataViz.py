First Viz :

ten_pop_songs = df.groupby('title')['listen_count'].count().reset_index()
                         .sort_values(by='listen_count', ascending=False).head(10)
plt.figure(figsize=(10, 6))
artist_listen_counts = df['title'].value_counts().head(10)
plt.pie(artist_listen_counts, labels=artist_listen_counts.index, autopct='%1.1f%%')
plt.title('Top 10 songs by Listen Count')
plt.show()

Second Viz :

ten_pop_artists  = df.groupby(['artist_name'])['listen_count'].count().reset_index().
                     sort_values(['listen_count', 'artist_name'], ascending = [0,1])
ten_pop_artists = ten_pop_artists[:10]
plt.figure(figsize=(10, 6))
sns.barplot(x='listen_count', y='artist_name', data=ten_pop_artists, palette='Set2')
plt.title('Top 10 des artistes par nombre d\'écoutes')
plt.xlabel('Nombre total d\'écoutes')
plt.ylabel('Artiste')
plt.show()

Third Viz :

plt.figure(figsize=(12, 8))
listen_count_by_year = df.groupby('year')['listen_count'].sum()
listen_count_by_year.plot()
plt.xlabel('Année')
plt.ylabel('Nombre total d\'écoutes')
plt.title('Nombre total d\'écoutes au fil du temps')
plt.show()

Fourth Viz :

plt.figure(figsize=(10, 6))
sns.histplot(df['year'], bins=20, kde=True)
plt.xlabel('Year')
plt.ylabel('Listen Count')
plt.title('Distribution of Listen Count by Year')
plt.show()

Fifth Viz :

numeric_columns = df[['listen_count', 'year', 'rating']]
correlation_matrix = numeric_columns.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matrice de corrélation des colonnes numériques')
plt.show()
