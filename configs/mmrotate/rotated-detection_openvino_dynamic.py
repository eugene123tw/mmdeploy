_base_ = [
    './rotated-detection_dynamic.py',
    '../_base_/backends/openvino.py'
]

onnx_config = dict(output_names=['dets', 'labels'], input_shape=None)

backend_config = dict(
    model_inputs=[dict(opt_shapes=dict(input=[1, 3, 800, 1344]))])
