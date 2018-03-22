import Augmentor

p = Augmentor.Pipeline("templates")

p.rotate_random_90(probability=0.7)
p.zoom(probability = 0.2, min_factor = 1.1, max_factor = 1.3)
p.skew(probability = 0.5)
p.random_distortion(probability = 0.7, grid_width = 100, grid_height = 100, magnitude = 5)
p.flip_random(probability=0.5)

p.sample(100)