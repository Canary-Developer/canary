# canary
A mutation analysis tool combining static analysis and instrumentation with a dynamic analysis to place mutants and generate graphs.

## Getting started
Activate the virtual environment *canary-env*.
```console
make install
make test
make run
```

Building the docker development image can be done by executing 
```console
make build
```

## Mutation analysis projects
### lib-hyrogen
In order to replicate the data presented in the paper with Canary, one must build canary Docker Image with ``make build`` and then clone [libhydrogen](https://github.com/Canary-Developer/canary-libhydrogen). When the Docker image ``canary:dev`` has been created then in your clone of [libhydrogen](https://github.com/Canary-Developer/canary-libhydrogen) run:
```console
make mutate
```
The resulting graphs and structure log files can be found in *mutation_analysis/* together with *data_parser.py* which handles the parsing of the data. In the *mutation_analysis_docker-compose.yml* the analysis configuration can be seen:
```console
      - mutate
      - --base=/input
      - --file=impl/Canary.h impl/common.h impl/core.h impl/gimli-core.h impl/hash.h impl/hydrogen_p.h impl/kdf.h impl/kx.h impl/pwhash.h impl/random.h impl/secretbox.h impl/sign.h impl/x25519.h impl/gimli-core/portable.h impl/gimli-core/sse2.h impl/random/avr.h impl/random/esp32.h impl/random/mbed.h impl/random/nrf52832.h impl/random/particle.h impl/random/riot.h impl/random/stm32.h impl/random/unix.h impl/random/wasi.h impl/random/windows.h
      - --out=./mutation_analysis
      - --build_command=make -C /input/ tests/tests
      - --test_command=/input/tests/tests
      - --placement_strategy=pathbased
      - --testing_backend=ffs_gnu_assert
      - --mutation_strategy=obom
      - --unit_whitelist=hydro_hash_init_with_tweak hydro_kx_aead_xor_enc hydro_kx_aead_xor_dec hydro_secretbox_encrypt_iv hydro_hex2bin hydro_kx_n_2 hydro_kx_n_1 hydro_kx_nk_1 hydro_sign_verify_core hydro_increment hydro_pwhash_derive_static_key hydro_kx_xx_2 hydro_random_u32 hydro_secretbox_xor_dec hydro_secretbox_xor_enc hydro_secretbox_probe_create hydro_secretbox_decrypt mem_cpy mem_xor hydro_random_ensure_initialized hydro_kx_kk_3 hydro_x25519_adc hydro_kx_xx_3 mem_xor2 hydro_pwhash_create hydro_sign_prehash hydro_secretbox_setup hydro_pwhash_reencrypt hydro_secretbox_final hydro_kx_nk_3 hydro_bin2hex hydro_sign_create hydro_kx_kk_2 hydro_sign_p2 hydro_secretbox_probe_verify hydro_kx_aead_encrypt hydro_kx_xx_1 hydro_random_buf_deterministic hydro_kx_aead_decrypt hydro_sign_keygen hydro_pwhash_deterministic hydro_kx_keygen hydro_equal hydro_kx_kk_1 hydro_random_ratchet hydro_hash_init hydro_hash_final hydro_kx_dh _hydro_pwhash_verify hydro_kx_xx_4 hydro_random_buf hydro_pwhash_verify hydro_kx_nk_2 hydro_hash_hash
```
