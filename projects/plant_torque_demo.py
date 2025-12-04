from ndeleh_fba import TorqueEvent, classify_torque_event


def demo_events() -> None:
    # Example 1: Clean, normal torque
    e1 = TorqueEvent(
        torque_value=32.0,
        target_min=30.0,
        target_max=35.0,
        is_red_flag=False,
        jam_detected=False,
        cycle_time=1.2,
        retries=0,
        manual_check_used=False,
    )

    # Example 2: Under-torque, red light, retries, jammed
    e2 = TorqueEvent(
        torque_value=24.0,
        target_min=30.0,
        target_max=35.0,
        is_red_flag=True,
        jam_detected=True,
        cycle_time=3.8,
        retries=3,
        manual_check_used=True,
    )

    # Example 3: Borderline – slightly high torque, 1 retry, no jam
    e3 = TorqueEvent(
        torque_value=36.5,
        target_min=30.0,
        target_max=35.0,
        is_red_flag=False,
        jam_detected=False,
        cycle_time=1.5,
        retries=1,
        manual_check_used=False,
    )

    for name, event in [("Normal", e1), ("Bad / jammed", e2), ("Borderline", e3)]:
        result = classify_torque_event(event)
        print(f"=== {name} ===")
        print(f"Severity: {result.severity.name}")
        print(f"Score:    {result.score:.1f}")
        print(f"Reason:   {result.reason}")
        print()


if __name__ == "__main__":
    demo_events()
