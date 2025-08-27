#!/usr/bin/env python3
"""
PDB Column Alignment Fixer
Fixes column alignment in PDB files according to PDB format specifications.
"""

def fix_pdb_alignment(input_file, output_file):
    """Fix PDB file column alignment according to PDB format standards."""
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                # Parse the line components
                parts = line.split()
                if len(parts) >= 11:
                    record_type = parts[0]
                    atom_num = parts[1]
                    atom_name = parts[2]
                    res_name = parts[3]
                    chain_id = parts[4]
                    res_num = parts[5]
                    x = parts[6]
                    y = parts[7]
                    z = parts[8]
                    occupancy = parts[9]
                    b_factor = parts[10]
                    element = parts[11] if len(parts) > 11 else ''
                    
                    # Format according to PDB specifications
                    # ATOM/HETATM: 1-6, atom_num: 7-11, atom_name: 13-16, res_name: 18-20
                    # chain: 22, res_num: 23-26, x: 31-38, y: 39-46, z: 47-54
                    # occupancy: 55-60, b_factor: 61-66, element: 77-78
                    
                    formatted_line = (
                        f"{record_type:<6}"      # cols 1-6
                        f"{atom_num:>5}"         # cols 7-11
                        f" "                     # col 12
                        f"{atom_name:<4}"        # cols 13-16
                        f" "                     # col 17
                        f"{res_name:>3}"         # cols 18-20
                        f" "                     # col 21
                        f"{chain_id:>1}"         # col 22
                        f"{res_num:>4}"          # cols 23-26
                        f"    "                  # cols 27-30 (insertion code + spaces)
                        f"{float(x):8.3f}"       # cols 31-38
                        f"{float(y):8.3f}"       # cols 39-46
                        f"{float(z):8.3f}"       # cols 47-54
                        f"{float(occupancy):6.2f}"  # cols 55-60
                        f"{float(b_factor):6.2f}"   # cols 61-66
                        f"          "            # cols 67-76 (spaces)
                        f"{element:>2}"          # cols 77-78
                        f"\n"
                    )
                    outfile.write(formatted_line)
                else:
                    # If the line doesn't have enough parts, write as-is
                    outfile.write(line)
            else:
                # For non-ATOM lines, write as-is
                outfile.write(line)

if __name__ == "__main__":
    input_file = "/workspaces/cPEPmatch/lib/test_system/1ycr-mod.pdb"
    output_file = "/workspaces/cPEPmatch/lib/test_system/1ycr-mod-fixed.pdb"
    
    fix_pdb_alignment(input_file, output_file)
    print(f"Fixed PDB file saved as: {output_file}")
