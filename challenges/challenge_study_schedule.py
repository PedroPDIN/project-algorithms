def study_schedule(permanence_period, target_time):
    size_period = len(permanence_period)
    count_period = 0

    for i in range(0, size_period):
        first = permanence_period[i][0]
        second = permanence_period[i][1]
        try:
            if first <= target_time <= second:
                count_period += 1
        except TypeError:
            return None

    return count_period
