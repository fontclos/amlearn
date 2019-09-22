from amlearn.utils.data import read_lammps_dump
from amlearn.featurize.featurizers.featurizer_pipeline import FeaturizerPipeline
from amlearn.featurize.featurizers.nearest_neighbor import VoroNN, DistanceNN
from amlearn.featurize.featurizers.short_range_order import \
    DistanceInterstice, VolumeAreaInterstice
from amlearn.featurize.featurizers.medium_range_order import MRO

"""
This is an example script of deriving interstice distribution features for 
each atom, based on relevant distance/area/volume interstice classes in 
amlearn.featurize.featurizers.short_range_order as well as classes in 
amlearn.featurize.featurizers.medium_range_order to further coarse SRO 
features to MRO. 
"""

system = ["Cu65Zr35", "qr_5plus10^10"]
atomic_number_list = [29, 40]

lammps_file = "xxx/dump.lmp"
structure, bds = read_lammps_dump(lammps_file)

output_path = "xxx/xxx"

featurizers = [
    # neighboring analysis
    VoroNN(bds=bds, cutoff=5, output_path=output_path),
    DistanceNN(bds=bds, cutoff=4, output_path=output_path),

    # distance interstice
    DistanceInterstice(atomic_number_list=atomic_number_list,
                       dependent_class='voro', output_path=output_path),
    DistanceInterstice(atomic_number_list=atomic_number_list,
                       dependent_class='dist', output_path=output_path),

    # area and volume interstice
    VolumeAreaInterstice(atomic_number_list=atomic_number_list,
                         output_path=output_path),

    # from SRO to MRO
    MRO(output_path=output_path)]

# defining a featurizer_pipeline
featurizer_pipeline = FeaturizerPipeline(featurizers=featurizers,
                                         output_path=output_path)

# featurization
feature_df = featurizer_pipeline.fit_transform(X=structure,
                                               bds=bds, lammps_df=structure)