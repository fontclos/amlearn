import os
import pandas as pd
from amlearn.featurize.featurizers.medium_range_order import MRO
from amlearn.utils.basetest import AmLearnTest

module_dir = os.path.dirname(os.path.abspath(__file__))


class TestMro(AmLearnTest):
    def setUp(self):
        pass
    #
    # def test_volume_area_interstice_mro(self):
    #     nn_df = pd.read_pickle(os.path.join(
    #         module_dir, 'data', 'featurizer_voro_nn.pickle.gz'))
    #
    #     sro_df = pd.read_pickle(os.path.join(
    #         module_dir, 'data', 'sro', 'featurizer_sro_voro_miracle_radius_'
    #                                    'volume_area_interstice.pickle.gz'))
    #     mro = MRO(output_file_name='volume_area_interstice_mro')
    #     result_df = mro.fit_transform(X=sro_df, dependent_df=nn_df)
    #     self.assertEqual(len(result_df.columns), 60)
    #     self.assertEqual(result_df.iloc[3, -1], -0.026078)
    #
    # def test_atomic_packing_mro(self):
    #     nn_df = pd.read_pickle(os.path.join(
    #         module_dir, 'data', 'featurizer_voro_nn.pickle.gz'))
    #
    #     sro_df = pd.read_pickle(os.path.join(
    #         module_dir, 'data', 'sro', 'featurizer_sro_voro_miracle_radius_'
    #                                    'atomic_packing_efficiency.pickle.gz'))
    #     mro = MRO(output_file_name='volume_area_interstice_mro')
    #     result_df = mro.fit_transform(X=sro_df, dependent_df=nn_df)
    #     print(result_df)
    #
    # def test_cluster_packing_mro(self):
    #     nn_df = pd.read_pickle(os.path.join(
    #         module_dir, 'data', 'featurizer_voro_nn.pickle.gz'))
    #
    #     sro_df = pd.read_pickle(os.path.join(
    #         module_dir, 'data', 'sro', 'featurizer_sro_voro_miracle_radius_'
    #                                    'cluster_packing_efficiency.pickle.gz'))
    #     mro = MRO(output_file_name='cluster_packing_efficiency_mro')
    #     result_df = mro.fit_transform(X=sro_df, dependent_df=nn_df)
    #     print(result_df)

    def test_all_interstice_and_packing_mro(self):
        nn_df = pd.read_pickle(os.path.join(
            module_dir, 'data', 'featurizer_voro_nn.pickle.gz'))

        sro_volume_area_df = pd.read_pickle(os.path.join(
            module_dir, 'data', 'sro', 'featurizer_sro_voro_miracle_radius_'
                                       'volume_area_interstice.pickle.gz'))
        cluster_packing_df = pd.read_pickle(os.path.join(
            module_dir, 'data', 'sro', 'featurizer_sro_voro_miracle_radius_'
                                       'cluster_packing_efficiency.pickle.gz'))
        atomic_packing_df = pd.read_pickle(os.path.join(
            module_dir, 'data', 'sro', 'featurizer_sro_voro_miracle_radius_'
                                       'atomic_packing_efficiency.pickle.gz'))
        all_df = cluster_packing_df.join(atomic_packing_df)
        all_df = all_df.join(sro_volume_area_df)
        mro = MRO(output_file_name='all_insterstice_and_packing_mro')
        result_df = mro.fit_transform(X=all_df, dependent_df=nn_df)
        self.assertEqual(len(result_df.columns), 72)
        self.assertEqual(result_df.iloc[3, -1], -0.026077608080648407)

    # def test_voro_index_mro(self):
    #     atoms_df = pd.read_csv(os.path.join(module_dir, 'data',
    #                                         'sro', 'featurizer_voro_index.csv'),
    #                            index_col=0)
    #     mro = MRO()
    #     result_df = mro.fit_transform(X=atoms_df)
    #     self.assertTrue('Voronoi idx5 voro sum_NN' in result_df.columns)
    #     self.assertEqual(len(result_df), len(atoms_df))
    #     self.assertAlmostEqual(result_df['Voronoi idx3 voro sum_NN'].iloc[0],
    #                            21445)
    #     self.assertAlmostEqual(result_df['Voronoi idx4 voro std_NN'].iloc[12],
    #                            5522.932)
    #     self.assertAlmostEqual(result_df['Voronoi idx4 voro diff_NN'].iloc[13],
    #                            -3)
    #
    # def test_character_motif_mro(self):
    #     atoms_df = pd.read_csv(os.path.join(module_dir, 'data', 'sro',
    #                                         'featurizer_character_motif.csv'),
    #                            index_col=0)
    #     mro = MRO()
    #     result_df = mro.fit_transform(X=atoms_df)
    #     print(result_df.head(10))
    #     self.assertTrue('Voronoi idx5 voro sum_NN' in result_df.columns)
    #     self.assertEqual(len(result_df), len(atoms_df))
    #     self.assertAlmostEqual(result_df['Voronoi idx3 voro sum_NN'].iloc[0],
    #                            21445)
    #     self.assertAlmostEqual(result_df['Voronoi idx4 voro std_NN'].iloc[12],
    #                            5522.932)
    #     self.assertAlmostEqual(result_df['Voronoi idx4 voro diff_NN'].iloc[13],
    #                            -3)
