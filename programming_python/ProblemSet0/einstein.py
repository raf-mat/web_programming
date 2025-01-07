def main():
    mass = int(input())
    print(energy(mass))

def energy(mass):
    return (mass * 300000000 ** 2)

main()
