def main():
    import psutil
    for key0, value0 in psutil.net_if_addrs().items():
        print("\n->", key0)
        for i, snicaddr in enumerate(value0):
            print(i,"family: {0} address: {1}, netmask: {2}, broadcast: {3}"
            .format(snicaddr.family.name, snicaddr.address, snicaddr.netmask, snicaddr.broadcast))

if __name__ == '__main__':
    main()