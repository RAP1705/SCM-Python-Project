import cv2
from pyzbar.pyzbar import decode

def scan_barcode_opencv():
    # Initialize the camera capture object
    cap = cv2.VideoCapture(0)
    barcode_detected = False
    text_barcode = None  # Ensuring text_barcode is defined

    try:
        while cap.isOpened():
            success, frame = cap.read()
            frame = cv2.flip(frame, 1)
            detected_barcode = decode(frame)

            if detected_barcode:
                for barcode in detected_barcode:
                    if barcode.data:
                        text_barcode = barcode.data.decode('utf-8')
                        cv2.putText(frame, text_barcode, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                        barcode_detected = True
                        break

            if barcode_detected:
                break  # Break out of the while loop if barcode is detected

            cv2.imshow('scanner', frame)
            if cv2.waitKey(1) == ord('q'):
                break  # Allow exit with 'q' key

    finally:
        # Ensure resources are released regardless of how the function exits
        cap.release()
        cv2.destroyAllWindows()

    return text_barcode  # Return the decoded barcode or None if nothing was detected

if __name__ == "__main__":
    print(scan_barcode_opencv())
