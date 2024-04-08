import ecole
import argparse
from pathlib import Path
#Pathlib module makes sure that your file paths work the same in different operating systems. 

import ecole.instance

def generate_instances(instances, lp_dir, n):
    lp_dir = Path(f"data/instances")/lp_dir
    lp_dir.mkdir(parents=True)
    for i in range(n):
        instance = next(instances)
        #The next() function returns the next item in an iterator
        filename = str(lp_dir/f"instance_{i+1}.lp")
        print(f' generating file {filename} ...')
        instance.write_problem(filename)


def generate_setcovers(n, folder_name, nrows, ncols, dens, rng):
    lp_dir = f"setcover/{folder_name}_{nrows}r_{ncols}c_{dens}d"
    instances = ecole.instance.SetCoverGenerator(n_rows=nrows, n_cols=ncols, density=dens, rng=rng)
    generate_instances(instances, lp_dir, n)


def generate_indsets(n, folder_name, number_of_nodes, affinity, rng):
    lp_dir = f"indset/{folder_name}_{number_of_nodes}_{affinity}"
    barabasi_albert = ecole.instance.IndependentSetGenerator.GraphType.barabasi_albert
    instances = ecole.instance.IndependentSetGenerator(n_nodes=number_of_nodes, affinity=affinity, graph_type=barabasi_albert, rng=rng)
    generate_instances(instances, lp_dir, n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('problem', help='MILP instance type to process.', choices=['setcover', 'indset'],)
    parser.add_argument('s', '--seed', help='Random generator seed (default 0).', default=0,)
    args = parser.parse_args()
    rng = ecole.spawn_random_generator()
    rng.seed(args.seed)

    if args.problem == 'setcover':
        nrows = 500
        ncols = 1000
        dens = 0.05
        max_coef = 100

        #train instances
        generate_setcovers(10000, "train", nrows, ncols, dens, rng)

        #validation instances
        generate_setcovers(2000, "valid", nrows, ncols, dens, rng)

        #small transfer instances
        generate_setcovers(100, "transfer", 500, ncols, dens, rng)

        #medium transfer instances
        generate_setcovers(100, "transfer", 1000, ncols, dens, rng)

        #big transfer instances
        generate_setcovers(100, "transfer", 2000, ncols, dens, rng)

        #test instances
        generate_setcovers(2000, "test", nrows, ncols, dens, rng)

        print('done.')

    elif args.problem == 'indset':
        number_of_nodes = 500
        affinity = 4

        #train instances
        generate_indsets(10000, "train", number_of_nodes, affinity, rng)

        #validation instances
        generate_indsets(2000, "valid", number_of_nodes, affinity, rng)

        #small transfer instances
        generate_indsets(100, "transfer", 500, affinity, rng)

        #medium transfer instances
        generate_indsets(100, "transfer", 1000, affinity, rng)

        #big transfer instances
        generate_indsets(100, "transfer", 2000, affinity, rng)

        #test instances
        generate_indsets(2000, "test", number_of_nodes, affinity, rng)

        print('done.')