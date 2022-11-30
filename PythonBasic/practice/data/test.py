weight_loss_n = [73,72,72,71,72,71,70,69,68,67,67,66,66,67,66,65]

loss_list = []
for i in range(0,15):
    loss = weight_loss_n[i] - weight_loss_n[i+1]
    loss_list.append(loss)

print(loss_list)

