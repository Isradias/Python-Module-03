import sys


def valid_inputs(list) -> int:
    nb = 0
    for arg in list:
        try:
            int(arg)
            nb += 1
        except Exception:
            pass
    return (nb)


if (__name__ == "__main__"):
    print("=== Player Score Analytics ===")

    try:
        score_len = valid_inputs(sys.argv)
        score = [0] * score_len
        i = 0
        for arg in sys.argv[1:]:
            try:
                score[i] = int(arg)
                i += 1
            except Exception:
                print(f"Invalid parameter: '{arg}'")
        if (score_len == 0):
            raise Exception("No scores provided. Usage: python3 "
                            "ft_score_analytics.py <score1> <score2> ...")
        print(f"Scores processed: {score}")
        print(f"Total players: {score_len}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score)/score_len}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}\n")
    except Exception as e:
        print(e)
