from __future__ import print_function
import pybilt.bilayer_analyzer.bilayer_analyzer as ba
def test_lipid_tilt():
    analyzer = ba.BilayerAnalyzer(structure='../pybilt/sample_bilayer/sample_bilayer.psf',
                                  trajectory='../pybilt/sample_bilayer/sample_bilayer_10frames.dcd',
                                  selection="resname POPC DOPE TLCL2")

    #remove the default msd analysis
    analyzer.remove_analysis('msd_1')
    analyzer.add_analysis("lipid_tilt lt leaflet lower resname POPC style order ref_axis z")
    analyzer.adjust_rep_setting('vector_frame', 'ref_atoms', {'DOPE':{'start':
                                                ['C218','C318'], 'end':'P'},
                                                'POPC':{'start':['C218', 'C316'],
                                                'end':'P'}, 'TLCL2':
                                                {'start':['CA18','CB18','CC18',
                                                 'CD18'], 'end':['P1', 'P3']}})
    analyzer.run_analysis()
    lt_dat = analyzer.get_analysis_data('lt')
    print('Lipid Tilts (vs time):')
    print(lt_dat)

if __name__ == '__main__':
    test_lipid_tilt()
