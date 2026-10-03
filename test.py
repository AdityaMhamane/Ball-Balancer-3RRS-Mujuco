import mujoco
import mujoco.viewer

# Load the model from your XML file
model = mujoco.MjModel.from_xml_path('scene.xml')
data = mujoco.MjData(model)

# Launch the interactive viewer
mujoco.viewer.launch(model, data)