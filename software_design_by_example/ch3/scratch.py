# %%
import hashlib

# %%

groups = []

with open("home_alone.txt", "r") as file:
    file_contents = file.readlines()

    for line in file_contents:
        if line.strip():  # ignore blank lines
            # print(line)

            hash_object = hashlib.sha256(line.encode("utf-8"))
            hexdigest = hash_object.hexdigest()
            integer_representation = int(hexdigest, 16)

            groups.append(float(integer_representation))

# %%
import matplotlib.pyplot as plt

plt.hist(groups, bins=20)
plt.xlabel("Groups")
plt.ylabel("Frequency")
plt.title("Histogram of Groups")
plt.show()
