import mujoco
import mujoco.viewer
import time
# Load the model from your XML file
model = mujoco.MjModel.from_xml_path('Final2OpenChain.xml')
data = mujoco.MjData(model)

servo_1_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, "leg1_ctrl")
servo_2_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, "leg2_ctrl")
servo_3_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, "leg3_ctrl")

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        step_start = time.time()

        # --- ACTUATOR CONTROL HAPPENS HERE ---
        
        # Option A: Control by specific ID (Safest method)
        data.ctrl[servo_1_id] = 0.00000  # Set target position to 0.5 radians
        data.ctrl[servo_2_id] = data.ctrl[servo_1_id] 
        data.ctrl[servo_3_id] = data.ctrl[servo_1_id]
        # Option B: Control by array index (Order matches the XML definition)
        # data.ctrl[0] = 0.5  # Controls "servo_1"
        # data.ctrl[1] = 10.0 # Controls "motor_1"

        # 4. Advance the physics simulation by 1 timestep
        mujoco.mj_step(model, data)

        # 5. Sync the viewer with the updated simulation data
        viewer.sync()

        # Maintain real-time simulation speed
        time_until_next_step = model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)


# Launch the interactive viewer
#mujoco.viewer.launch(model, data)