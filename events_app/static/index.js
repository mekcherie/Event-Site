function returningGuestChanged (isChecked) {
    console.log(isChecked)
    const newGuestInfo = document.getElementById('new-guest-info')
    if (isChecked) {
      newGuestInfo.style.display = 'none'
    } else {
      newGuestInfo.style.display = 'block'
    }
  }