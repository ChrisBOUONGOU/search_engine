from indexer import build_index
from search import search

def main():
    print("🔧 Indexation in progress...")
    build_index("data")

    print("✅ Ready ! write your research.\n")

    while True:
        query = input("🔎 Research : ")

        if query.lower() == "exit":
            break

        results = search(query)

        if not results:
            print("❌ Not found\n")
            continue

        print("\n📄 Result :")
        for doc, score in results:
            print(f"{doc} (score: {score:.4f})")

        print("\n")

if __name__ == "__main__":
    main()