def word_counter(file_name):
    """This function counts the words from file! \
    Return's word dictionary."""
    word_dict = {}
    with open(file_name) as f:
        for line in f:
            for chr in (",", "!"):
                line = line.replace(chr, "")
            for word in line.split():
                if word_dict.get(word):
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    total = sum(word_dict.values())
    word_dict.update(total=total)
    return word_dict


def result(file_name, word_dict):
    """Writes the results to the file! """
    with open(file_name, "w") as f:
        total = word_dict.pop("total")
        f.write(f"words: {word_dict}.\n")
        f.write(f"total: {total}")


if __name__ == "__main__":
    words = word_counter("example")
    result("results", words)
    print(words)
