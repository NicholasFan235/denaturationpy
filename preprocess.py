#!/usr/bin/python
# Process PDB file for mcce calculation
import sys
removable_res=[" ZN", "PCA", "XYP", " NA", " CL", " CA", " MG", " MN", "HOH"]


def preprocess_pdb(lines, chainID):
   newlines = []
   model_start = False
   for line in lines:
      if line[:5] == "MODEL":
         model_start = True
      
      if model_start and line[:6] == "ENDMDL":
         break
      
      if line[:6] != "ATOM  " and line[:6] != "HETATM":
         continue # discard non ATOM records
      
      if chainID:
         if not line[21] in chainID:
            continue # skip 

      if line[13] == "H" or line[12] == "H":
         continue
      
      if line[16] == "A":
         line = line[:16]+" "+line[17:]
      elif line[16] != " ":
         continue # delete this line, alternative posion is not A or empty

      if line[:6] == "HETATM" and line[17:20] == "MSE":
         if line[12:15] == "SE ":
            line = "ATOM  "+line[6:12]+" SD"+line[15:17]+"MET"+line[20:]
         else:
            line = "ATOM  "+line[6:17]+"MET"+line[20:]
      
      res = line[17:20]
      if res in removable_res:
         continue
      newlines.append(line)

   return newlines

if __name__ == "__main__":
   n=len(sys.argv)
   if n<2:
      print("preprocess.py pdbfile [chainID]")
      print("   This program will")
      print("   1) strip lines other than ATOM and HETATM records")
      print("   2) keep the first model of an NMR structure")
      print("   3) delete H and D atoms")
      print("   4) MSE to MET residue")
      print("   5) keep only one atom alternate position")
      print("   6) keep defined chains, if chain ID(s) are given in command")
      print("   7) remove some cofactors and salt ions")
      sys.exit(0)


   lines=open(sys.argv[1]).readlines()
   if len(sys.argv) > 2:
      chainID = sys.argv[2].upper()
   else:
      chainID = ""
     
   newlines = preprocess_pdb(lines, chainID)
   sys.stdout.writelines(newlines)
