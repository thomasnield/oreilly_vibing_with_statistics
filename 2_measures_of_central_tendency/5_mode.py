from scipy.stats import mode

dining_party_size = [1,2,2,2,2,2,3,3,
                     4,4,4,4,5,7,9,11]

mode, ct = mode(dining_party_size)

# Mode: 2, Count: 5
print(f"Mode: {mode}, Count: {ct}")