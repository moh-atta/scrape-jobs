import scrap_jobs

new_feature = ["New", "Branch", "Test"]

def titles():
    df = scrap_jobs.scrap()
    titles = df['Title'].tolist()
    return titles

if __name__ == '__main__':
    print(titles())
