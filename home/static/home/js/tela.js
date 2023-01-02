function changeOptions(opcao) {
    const options = {
      REC: {

        0: 'Selecione...',
        A: 'ASN',
        I: 'iLPN',
        V: 'VERIFY'
      },
      ARM: {
        0: 'Selecione...',
        L: 'LPN',
        D: 'DROP'
      },
      EXP: {
        0: 'Selecione...',
        T: 'TESTE',
        X: 'XTEST'
      },

      DEV: {
        0: 'Selecione...',
        H: 'HTESTE',
        Y: 'YTEST'
      },

    }

    const optionsToOpcao = options[opcao]

    const select = document.querySelector('#iproc')

    select.innerHTML = ''

    for (const [value, text] of Object.entries(optionsToOpcao)) {
      const option = document.createElement('option')
      option.textContent = text
      option.value = value

      select.appendChild(option)
    }
  }