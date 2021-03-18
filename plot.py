def plot_wave(buf_ecg_qrs, sub_arr_beat, sub_arr_type, qrs_onset, qrs_offset, t_peak, t_offset, p_onset, plot_pt=False):

    times = np.arange(len(buf_ecg_qrs), dtype=float)
    times /= SAMPLING_RATE
    plt.plot(times, buf_ecg_qrs)

    [plt.plot(times[sub_arr_beat[i]], buf_ecg_qrs[sub_arr_beat[i]], 'ko') for i in range(len(sub_arr_beat)) if
     sub_arr_type[i] == 1.0]
    [plt.plot(times[sub_arr_beat[i]], buf_ecg_qrs[sub_arr_beat[i]], 'ro') for i in range(len(sub_arr_beat)) if
     sub_arr_type[i] == 60.0]
    [plt.plot(times[sub_arr_beat[i]], buf_ecg_qrs[sub_arr_beat[i]], 'yo') for i in range(len(sub_arr_beat)) if
     sub_arr_type[i] == 70.0]
    if plot_pt:
        qrs_onset = qrs_onset[qrs_onset < len(buf_ecg_qrs)]
        qrs_offset = qrs_offset[qrs_offset < len(buf_ecg_qrs)]
        t_peak = t_peak[t_peak < len(buf_ecg_qrs)]
        t_offset = t_offset[t_offset < len(buf_ecg_qrs)]
        p_onset = p_onset[p_onset < len(buf_ecg_qrs)]

        [plt.plot(times[qrs_onset[i]], buf_ecg_qrs[qrs_onset[i]], 'm*') for i in range(len(qrs_onset)) if
         sub_arr_beat[i] > 0]
        [plt.plot(times[qrs_offset[i]], buf_ecg_qrs[qrs_offset[i]], 'm+') for i in range(len(qrs_offset)) if
         sub_arr_beat[i] > 0]
        [plt.plot(times[t_peak[i]], buf_ecg_qrs[t_peak[i]], 'gs') for i in range(len(t_peak)) if
         sub_arr_beat[i] > 0]
        [plt.plot(times[t_offset[i]], buf_ecg_qrs[t_offset[i]], 'gh') for i in range(len(t_offset)) if
         sub_arr_beat[i] > 0]
        [plt.plot(times[p_onset[i]], buf_ecg_qrs[p_onset[i]], 'cp') for i in range(len(p_onset)) if
         sub_arr_beat[i] > 0]

    plt.show()

    @staticmethod
    def plot_numpy_array_to_figure(array, order_figure, name_figure):
        plt.figure(order_figure)
        plt.plot(array)
        plt.xlabel('Numper sample (sample)')
        plt.ylabel('voltage (mV)')
        plt.title(name_figure)
        plt.grid(True)
        plt.show(block=False)

    @staticmethod
    def plot_numpy_array_to_figure_mark_peaks(array, order_figure, name_figure, beats):
        time = np.arange(start=0, stop=len(array), step=1, dtype=np.int)
        array = list(map(float, array[:]))
        array = np.asarray(array, dtype=float)
        v_beat = array[beats]
        plt.figure(order_figure)
        plt.plot(time, array[0:len(array)])
        plt.plot(time[beats], v_beat, 'ro')
        plt.xlabel('Numper sample (sample)')
        plt.ylabel('voltage (mV)')
        plt.title(name_figure)
        plt.grid(True)
        plt.show(block=False)

