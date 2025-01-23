import axengine as axe
import numpy as np

def main():
    try:
        #dummy_data = np.random.randint(0, 255, (1, 640, 640, 3), dtype=np.uint8)
        session = axe.InferenceSession('yolo11s.axmodel')
        input_data = np.random.randint(0, 255, (1, 640, 640, 3), dtype=np.uint8)
        outputs = session.run([o.name for o in session.get_outputs()], 
                           {session.get_inputs()[0].name: input_data})
        
        np.save('outputs.npy', outputs[0])
        print("Outputs saved to outputs.npy")
        
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
