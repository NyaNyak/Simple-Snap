f'Frame: {frame}/{frame_total}, Speed: x{speed_table[speed_index]:.2g}'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))