import sys
from test_generator.generator import generate_test_cases


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<feature description>\"")
        return

    feature_description = sys.argv[1]

    print("\n[INFO] Generating test cases...\n")

    test_cases = generate_test_cases(feature_description)

    print(test_cases)


if __name__ == "__main__":
    main()