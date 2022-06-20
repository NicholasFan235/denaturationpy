import Bio.PDB as bpdb
import numpy as np

class Featurizer:
    def __init__(self, pdb: str):
        struct = bpdb.PDBParser().get_structure(pdb[:4], f'pdb_files/{pdb}.pdb')
        self.model = struct[0]
        self.pdb = pdb
        self.n_residues = len(list(self.model.get_residues()))

        self.dist_matrix = self._calc_dist_matrix(list(struct.get_residues()),
            list(struct.get_residues()), self._calc_min_dist)
        self.ca_dist_matrix = self._calc_dist_matrix(list(struct.get_residues()),
            list(struct.get_residues()), self._calc_residue_dist)

    def calculate_RCO(self, R_cutoff:float=6.0):
        RCO_tmp = 0 # Non-Normalized RCO
        N = 0
        for i, r1 in enumerate(list(self.model.get_residues())):
            for j, r2 in enumerate(list(self.model.get_residues())):
                if i>=j: continue
                if self.dist_matrix[i][j] > R_cutoff: continue
                atom_dist_matrix = self._calc_atom_dist_matrix(r1, r2)

                n = np.sum(np.triu(atom_dist_matrix <= R_cutoff))
                N += n
                RCO_tmp += abs(j-i) * n
        return RCO_tmp/(N*self.dist_matrix.shape[0])

    def calculate_ACO(self, R_cutoff:float=6.0):
        RCO_tmp = 0 # Non-Normalized ACO
        N = 0
        for i, r1 in enumerate(list(self.model.get_residues())):
            for j, r2 in enumerate(list(self.model.get_residues())):
                if i>=j: continue
                if self.dist_matrix[i][j] > R_cutoff: continue
                atom_dist_matrix = self._calc_atom_dist_matrix(r1, r2)

                n = np.sum(np.triu(atom_dist_matrix <= R_cutoff))
                N += n
                RCO_tmp += abs(j-i) * n
        return RCO_tmp/N

    def _calc_residue_dist(residue_one, residue_two) :
        """Returns the C-alpha distance between two residues"""
        diff_vector  = residue_one["CA"].coord - residue_two["CA"].coord
        return np.sqrt(np.sum(diff_vector * diff_vector))

    def _calc_min_dist(r1, r2):
        m = np.inf
        for a1 in r1.get_atoms():
            if a1.name == 'H': continue
            for a2 in r2.get_atoms():
                if a2.name == 'H': continue
                v = a1.coord - a2.coord
                d = np.sqrt(np.sum(v*v))
                m = min(d, m)
        return m
                

    def _calc_dist_matrix(chain_one, chain_two, distance_metric) :
        """Returns a matrix of C-alpha distances between two chains"""
        answer = np.zeros((len(chain_one), len(chain_two)), float)
        for row, residue_one in enumerate(chain_one) :
            for col, residue_two in enumerate(chain_two) :
                answer[row, col] = distance_metric(residue_one, residue_two)
        return answer

    def _calc_atom_dist_matrix(r1, r2):
        matrix = np.zeros((len(list(r1.get_atoms())), len(list(r2.get_atoms()))))
        for i, a1 in enumerate(r1.get_atoms()):
            for j, a2 in enumerate(r2.get_atoms()):
                if a1.name == 'H' or a2.name == 'H': matrix[i,j] = np.nan
                v = a1.coord - a2.coord
                matrix[i,j] = np.sqrt(np.sum(v*v))
        return matrix

