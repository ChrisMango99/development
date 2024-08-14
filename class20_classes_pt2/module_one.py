print('I will run from Module two', __name__)

def main():

    # Is this file being run directly by Python or is it being run indirectly?
    print('I will run from module 1 directly but not module two', __name__)

if __name__ == '__main__':
    main()