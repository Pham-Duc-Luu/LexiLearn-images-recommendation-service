import math


def combine_result(scores):
    result = {}
    balance = 1 / len(scores)
    for _, img_scores in scores.items():
        for img, score in img_scores.items():
            if result.get(img) is None:
                result[img] = 0
            result[img] += score * balance
    return result


def get_batch_img(scores, start_idx, interval):
    return scores[start_idx:start_idx + interval]


def rank_img(result, reverse=True):
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=reverse))


def bm25_get_image(words, bag_of_words, doc_freq, k=1.2, beta=0.75, reverse=True):
    scores = {}
    for word in words:
        scores[word] = {}

    n_doc = bag_of_words["_n_img"]
    for word in words:
        if doc_freq.get(word) is None:
            scores[word]["Err: Non existing word"] = -1
            continue

        for img, bag in bag_of_words.items():
            if img == "_avg_len" or img == "_n_img" or img == "_n_sample":
                continue

            idf = math.log(1 + (n_doc - doc_freq[word] + 0.5) / (doc_freq[word] + 0.5))

            # Words not exist in the bag
            if bag.get(word) is None:
                continue

            tf = (k + 1) * bag[word] / (
                    k * (1 - beta + beta * bag["_len"] / (bag_of_words["_avg_len"] * bag["_n_appear"])) + bag[word])
            scores[word][img] = idf * tf

    # Combining the results
    result = combine_result(scores)

    # Ranking
    result = rank_img(result, reverse)

    return result
